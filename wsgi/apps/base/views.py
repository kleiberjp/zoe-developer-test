# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.template.loader import render_to_string

from apps.agent.forms import AgentsForm
from apps.contact.models import Contact
from apps.agent.models import Agent
from project import utils

from pyzipcode import ZipCodeDatabase
from pyzipcode import ZipNotFoundException
import csv
import codecs

DEFAULT_RAIDUS = 20


class WebSiteViewClass(View):
    template_name = 'pages/home.html'

    def get(self, request):
        form = AgentsForm()
        context = {
            "agentform": form
        }
        return render_to_response(
            self.template_name,
            context,
            context_instance=RequestContext(request)
        )


class AgentsMatchViewClass(View):
    def post(self, request):
        form = AgentsForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return utils.form_invalid(form)

    def form_valid(request, form):
        zcdb = ZipCodeDatabase()
        agent1_zipcode = form.cleaned_data['zipcode_agent1']
        agent2_zipcode = form.cleaned_data['zipcode_agent2']

        agent1, created = Agent.objects.update_or_create(
            name='Agent 1',
            defaults={'zipcode': agent1_zipcode}
        )

        agent2, created = Agent.objects.update_or_create(
            name='Agent 2',
            defaults={'zipcode': agent2_zipcode},
        )

        nearestzipcode_a1 = []
        nearestzipcode_a2 = []
        try:
            nearestzipcode_a1 = [z.zip for z in zcdb.get_zipcodes_around_radius(agent1_zipcode, DEFAULT_RAIDUS)]
        except ZipNotFoundException:
            pass

        try:
            nearestzipcode_a2 = [z.zip for z in zcdb.get_zipcodes_around_radius(agent2_zipcode, DEFAULT_RAIDUS)]
        except ZipNotFoundException:
            pass

        if nearestzipcode_a1 or nearestzipcode_a2:
            nearestzipcode_a2 = [x for x in nearestzipcode_a2 if not (x in nearestzipcode_a1)]

            contacts_agent1 = Contact.objects.filter(zipcode__in=nearestzipcode_a1).all()
            contacts_agent2 = Contact.objects.filter(zipcode__in=nearestzipcode_a2).all()

            if contacts_agent1 or contacts_agent2:
                data = {
                    'agent1': agent1,
                    'contact_agent1': contacts_agent1,
                    'agent2': agent2,
                    'contact_agent2': contacts_agent2
                }
                content = render_to_string('website/matchs-agent-modal.html', data)
                context = {
                    'success': True,
                    'matchs': content
                }
            else:
                context = {
                    'hasErrors': False,
                    'hasMessage': True,
                    'message': utils.NOT_MATCH_EXIST,
                    'success': False,
                }
        else:
            context = {
                'hasErrors': False,
                'hasMessage': True,
                'message': utils.NOT_MATCH_EXIST,
                'success': False,
            }
        return utils.render_to_json(context)


class ContactLoadCSVViewClass(View):
    def post(self, request):
        if request.FILES:
            csvfile = request.FILES['csv_file']
            dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
            csvfile.open()
            reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
            next(reader)
            for row in reader:
                if len(row) <= 2:
                    Contact.objects.update_or_create(name=row[0], zipcode=row[1])
                    context = {
                        'hasErrors': False,
                        'hasMessage': False,
                        'message': utils.SUCCESS_UPLOAD,
                        'success': True,
                    }
                else:
                    context = {
                        'hasErrors': False,
                        'hasMessage': True,
                        'message': utils.BAD_FILE,
                        'success': False,
                    }

        else:
            context = {
                'hasErrors': False,
                'hasMessage': True,
                'message': utils.ADD_FILE,
                'success': False,
            }
        return utils.render_to_json(context)
