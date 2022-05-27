superficie= "56365 km2"
num_hombres= 1494815
num_mujeres= 1532128
temp= 25.45
clima= "calido, subhumedo, seco y semiseco"
culiacan= 0.3315
mazatlan= 0.1657
poblacion_total= num_hombres+num_mujeres
pt= str(poblacion_total)
print( "La poblacion total es de: "+pt+" habitantes")

ttotal_cul= round(culiacan*poblacion_total)
poblacion_culiacan= str(ttotal_cul)
total_maz= round(mazatlan*poblacion_total)
poblacion_mazatlan=str(total_maz)
print( "La poblacion total en el municipio de culiacan es de " + poblacion_culiacan + "  habitantes, mientras que la de Mazatlan es de " +poblacion_mazatlan+ " habitantes")
temp_cadena=str(temp)
print( "El tipo de clima en Sinaloa es "+clima+ ". Su temperatura media es de " +temp_cadena+ " grados")