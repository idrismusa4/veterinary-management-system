# management/management/commands/populate_inventory.py
import random
from django.core.management.base import BaseCommand
from hospAdmin.models import *

class Command(BaseCommand):
    help = 'Populate the drug inventory'

    def handle(self, *args, **kwargs):
        drugs = [
            ('Amoxicillin', 100, 'Antibiotics'),
            ('Clavamox', 50, 'Antibiotics'),
            ('Cephalexin', 75, 'Antibiotics'),
            ('Doxycycline', 30, 'Antibiotics'),
            ('Metronidazole', 40, 'Antibiotics'),
            ('Enrofloxacin', 60, 'Antibiotics'),
            ('Ivermectin', 100, 'Antiparasitics'),
            ('Fenbendazole', 20, 'Antiparasitics'),
            ('Praziquantel', 15, 'Antiparasitics'),
            ('Pyrantel Pamoate', 35, 'Antiparasitics'),
            ('Selamectin', 25, 'Antiparasitics'),
            ('Rabies Vaccine', 200, 'Vaccines'),
            ('Distemper/Parvo Vaccine', 150, 'Vaccines'),
            ('Feline Leukemia Vaccine', 100, 'Vaccines'),
            ('Bordetella Vaccine', 80, 'Vaccines'),
            ('Lyme Disease Vaccine', 90, 'Vaccines'),
            ('Carprofen', 120, 'Anti-inflammatory and Pain Relief'),
            ('Meloxicam', 70, 'Anti-inflammatory and Pain Relief'),
            ('Prednisone', 60, 'Anti-inflammatory and Pain Relief'),
            ('Gabapentin', 50, 'Anti-inflammatory and Pain Relief'),
            ('Tramadol', 30, 'Anti-inflammatory and Pain Relief'),
            ('Propofol', 20, 'Anesthetics and Sedatives'),
            ('Isoflurane', 15, 'Anesthetics and Sedatives'),
            ('Ketamine', 25, 'Anesthetics and Sedatives'),
            ('Medetomidine', 10, 'Anesthetics and Sedatives'),
            ('Diazepam', 45, 'Anesthetics and Sedatives'),
            ('Heartgard', 90, 'Heartworm Preventatives'),
            ('Interceptor', 50, 'Heartworm Preventatives'),
            ('Revolution', 75, 'Heartworm Preventatives'),
            ('Frontline', 60, 'Flea and Tick Treatments'),
            ('Bravecto', 40, 'Flea and Tick Treatments'),
            ('NexGard', 30, 'Flea and Tick Treatments'),
            ('Advantage', 50, 'Flea and Tick Treatments'),
            ('Levothyroxine', 80, 'Hormones and Endocrine Drugs'),
            ('Insulin', 60, 'Hormones and Endocrine Drugs'),
            ('Methimazole', 50, 'Hormones and Endocrine Drugs'),
            ('Famotidine', 100, 'Gastrointestinal Medications'),
            ('Metoclopramide', 70, 'Gastrointestinal Medications'),
            ('Sucralfate', 40, 'Gastrointestinal Medications'),
            ('Maropitant', 30, 'Gastrointestinal Medications'),
            ('Tobramycin', 25, 'Ophthalmic and Otic Medications'),
            ('Cyclosporine', 15, 'Ophthalmic and Otic Medications'),
            ('Otomax', 35, 'Ophthalmic and Otic Medications'),
            ('Enrofloxacin Ear Drops', 20, 'Ophthalmic and Otic Medications'),
            ('Pimobendan', 50, 'Cardiovascular Drugs'),
            ('Enalapril', 45, 'Cardiovascular Drugs'),
            ('Furosemide', 40, 'Cardiovascular Drugs'),
            ('Atenolol', 35, 'Cardiovascular Drugs'),
            ('Euthanasia Solution', 10, 'Miscellaneous'),
            ('Activated Charcoal', 25, 'Miscellaneous'),
            ('Sterile Saline Solution', 50, 'Miscellaneous'),
        ]

        statuses = ['available', 'out of stock', 'refill soon']

        for drug in drugs:
            Inventory.objects.create(
                name=drug[0],
                quantity=drug[1],
                category=drug[2],
                status=random.choice(statuses)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the drug inventory'))
