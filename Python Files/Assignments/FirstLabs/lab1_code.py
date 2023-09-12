class Conversions ():
        
#Question 1
    #Part 1
    met_per_sec = 9.9979e8
    cm_per_sec = met_per_sec*100
    in_per_sec = cm_per_sec/2.54
    ft_per_sec = in_per_sec/12
    mi_per_sec = ft_per_sec/5280
    #mi_per_sec == 186280.86972083035

    #Part 2
    mi_per_min = mi_per_sec*60
    mi_per_hr = mi_per_min*60
    #mi_per_hr == 670611130.9949892
    
    #Question 2
    hr_to_earth = 93e6/mi_per_hr
    #hr_to_earth == 0.13867947563294308
    min_to_earth = hr_to_earth*60
    #min_to_earth == 8.320768537976585
    sec_to_earth = min_to_earth*60
    #sec_to_earth == 499.2461122785951
    
#Question 3
    kg_per_li = 1
    kg_per_cm3 = kg_per_li/1000
    cm3_in_in3 = 2.54**3
    kg_per_in3 = kg_per_cm3*cm3_in_in3
    in3_in_ft3 = 12**3
    kg_per_ft3 = kg_per_in3*in3_in_ft3

    lb_per_ft3 = kg_per_ft3*2.204
    #lb_per_ft3 == 62.41032988876802
    
    lb_per_gal = 8.33

    li_in_gal = 3.785
    cm3_in_gal = li_in_gal*1000
    in3_in_gal = cm3_in_gal/cm3_in_in3
    #in3_in_gal == 230.97487139856167

    #in^3 of a gal
    #lbs of a gal

#Question 4
    weight_of_humanity = 140*7e9
    ft3_to_mi3 = 5280**3
    lb_per_mi3 = lb_per_ft3*ft3_to_mi3
    volume_of_humanity = weight_of_humanity/lb_per_mi3
    #volume_of_humanity == 0.10667627196340702

#Question 5
    ft3_in_acre = (1/640*5280**2)
    ft3_in_gal = in3_in_gal/in3_in_ft3
    gal_in_acreft = ft3_in_acre/ft3_in_gal
    lb_per_acreft = gal_in_acreft*lb_per_gal
    ton_per_acreft = lb_per_acreft/2000
    #ton_per_acre == 1357.3188516209832