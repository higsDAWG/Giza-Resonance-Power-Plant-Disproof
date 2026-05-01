import math

def calculate_potential():
    print("--- Giza Power Plant Simulation ---")
    pressure_tonnes = 6000000 
    area_m2 = 52.5 # Área da Câmara do Rei
    quartz_constant = 2.3e-12 # Constante d31 do quartzo (C/N)
    
    force_newtons = pressure_tonnes * 1000 * 9.81
    stress = force_newtons / area_m2
    
    print(f"Força Gravitacional: {force_newtons:.2e} N")
    print(f"Tensão no Quartzo: {stress:.2e} Pa")
    print("Status: Potencial Piezoelétrico Ativo.")

if __name__ == "__main__":
    calculate_potential()
