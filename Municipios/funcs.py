def get_by_ine(dataset, ine_code):
    result = None
    for mun in dataset:
        if mun[2] == ine_code:
            result = mun
    return result

def get_largest(dataset):
    current_area = 0
    largest_mun = None
    for mun in dataset:
        if float(mun[-2]) > float(current_area):
            current_area = mun[-2]
            largest_mun = mun
    return largest_mun

def sup_total(dataset):
    area_counter = 0
    for mun in dataset:   
        area_counter += float(mun[-2])
    return round(area_counter)

def densidad_total(dataset):
    den_counter = 0
    for mun in dataset:
        den_counter += float(mun[-1])
    return round(den_counter)

def pob_total(dataset):
    result = []
    for mun in dataset:
        result.append(float(mun[-2])*float(mun[-1]))
    return round(sum(result))

def ley_bendford(dataset):
    densities = [mun[-1] for mun in dataset]
    result = {}
    for num in range(1,10):
        result[str(num)] = 0
    for density in densities:
        result[density[0]] += 1/len(densities)
    for k, v in result.items():
        print(f"{k}: {v}")
    

def menu():
    print("\n"*5 + " Bienvenido a la base de datos de los Municipios de la CAM ".center(150, "*")+ "\n")
    print("1. Buscar por INE del Municipio: " + (" " * (150 - len("1. Buscar por INE del Municipio: "))) + "#" + "\n")
    print("2. Cuál es el Municipio más grande de la CAM?"+ (" " * (150 - len("2. Cuál es el Municipio más grande de la CAM?"))) + "#" + "\n")
    print("3. Sepa cuál es la Superficie de la CAM"+ (" " *(150 - len("3. Sepa cuál es la Superficie de la CAM"))) + "#" + "\n")
    print("4. Sepa la densidad de población por km2 de la CAM"+ (" " *(150 - len("4. Sepa la densidad de población de la CAM"))) + "#" + "\n")
    print("5. Población total de la CAM"+ (" " *(150 - len("5. Población total de la CAM"))) + "#" + "\n")
    print("6. Sepa la población media por Municipio de la CAM"+ (" " *(150 - len("6. Sepa la población media por Municipio de la CAM"))) + "#" + "\n")
    print("7. Cómo aplica la Ley de Bendford en la CAM"+ (" " * (150 - len("7. Cómo aplica la Ley de Bendford en la CAM"))) + "#" + "\n")
    print("Q. Pulsa Q para salir" + (" " * (150 - len("Q. Pulsa Q para salir"))) + "#" + "\n")
