from django.db import models

class Catalogue(models.Model):
    class Meta:
        app_label="ricercar"

    RISM_A = 'RA'
    RISM_B = 'RB'
    CENSUS = 'CE'
    VOGEL = 'VO'
    BROWN = 'BR'
    HEARTZ = 'HE'
    VANHULST = 'VA'
    LESURE = 'LE'
    POGUE = 'PO'
    AGEE = 'AG'
    BERNSTEIN = 'BE'
    BOETTICHER = 'BO'
    BOORMAN = 'BO'
    GUILLO = 'GU'
    LEWIS = 'LW'
    SARTORI = 'SA'
    WEAVER = 'WE'

    CHOIX_CATALOGUE = (
        (RISM_A, 'Rism A'),
        (RISM_B, 'Rism B'),
        (CENSUS,'Census'),
        (VOGEL,'Vogel'),
        (BROWN,'Brown'),
        (HEARTZ,'Hearz'),
        (VANHULST,'Vanhulst'),
        (LESURE,'Lesure'),
        (POGUE,'Pogue'),
        (AGEE,'Agee'),
        (BERNSTEIN,'Bernstein'),
        (BOETTICHER,'Boetticher'),
        (BOORMAN,'Boorman'),
        (GUILLO,'Guillo'),
        (LEWIS,'Lewis'),
        (SARTORI,'Sartori'),
        (WEAVER,'Weaver'),
    )

    #now i don't know use that... depend of CESR. I think we have

    choix_catalogue = models.CharField(max_length=2, choices=CHOIX_CATALOGUE, default=RISM_A )
    #but i don't know after.