from Data_Base import session, Refacciones,Contenido

refacciones = [
    ("Filtros de aceite", "Bosch 3330", 20, 15.99),
    ("Filtros de aire", "Mann C 3698/3-2", 30, 12.50),
    ("Aceite de motor", "Castrol GTX 5W-30", 50, 24.99),
    ("Líquido de frenos", "Prestone DOT 3", 40, 7.99),
    ("Líquido de transmisión", "Valvoline ATF", 25, 17.49),
    ("Bujías", "NGK 7090", 60, 4.99),
    ("Juntas del motor", "Fel-Pro HS26170PT", 15, 45.00),
    ("Pistones", "Mahle 224-3888WR", 18, 55.00),
    ("Válvulas", "DNJ V3307", 22, 8.50),
    ("Correas de distribución", "Gates TCKWP312", 19, 85.00),
    ("Pastillas de freno", "Bosch BC905", 45, 29.99),
    ("Discos de freno", "ACDelco 18A925A", 32, 40.00),
    ("Tambores de freno", "DuraGo BDrum63001", 27, 35.00),
    ("Calipers de freno", "Raybestos FRC11879N", 16, 60.00),
    ("Embragues", "LUK 05-065", 20, 120.00),
    ("Cajas de cambios", "Aisin WCT-070", 15, 300.00),
    ("Convertidores de par", "Dacco A20", 17, 140.00),
    ("Ejes de transmisión", "Cardone 66-1009", 22, 70.00),
    ("Amortiguadores", "Monroe 58620", 40, 50.00),
    ("Resortes", "Moog 81069", 25, 30.00),
    ("Brazos de control", "Dorman 520-164", 19, 55.00),
    ("Rótulas", "TRW JBJ889", 29, 25.00),
    ("Cremalleras de dirección", "A1 Cardone 97-1000", 18, 200.00),
    ("Compresores de aire acondicionado", "UAC CO 4918AC", 17, 220.00),
    ("Condensadores", "Spectra Premium 7-4411", 24, 100.00),
    ("Filtros de cabina", "Fram CF10134", 50, 12.00),
    ("Ventiladores", "Dorman 620-232", 20, 90.00),
    ("Termostatos", "Stant 45359", 40, 15.00),
    ("Neumáticos", "Michelin Defender T+H", 35, 150.00),
    ("Rines", "American Racing AR172", 18, 200.00),
    ("Balanceadores de ruedas", "Hunter GSP9700", 16, 3000.00),
    ("Sensores de presión de neumáticos", "Schrader 20008", 28, 45.00),
    ("Válvulas de neumáticos", "Dill VS-90", 55, 5.00),
    ("Alternadores", "Bosch AL9962N", 21, 130.00),
    ("Arranques", "Denso 280-0112", 18, 150.00),
    ("Baterías", "Optima 8004-003", 20, 200.00),
    ("Fusibles", "Bussmann BP/ATM-15-RP", 75, 1.50),
    ("Sensores electrónicos", "Delphi SS10416", 25, 30.00),
    ("Silenciadores", "Flowmaster 942551", 22, 85.00),
    ("Catalizadores", "MagnaFlow 27402", 19, 300.00),
    ("Tubos de escape", "Walker 53206", 30, 40.00),
    ("Sensores de oxígeno", "Denso 234-4209", 35, 50.00),
    ("Colectores de escape", "Dorman 674-590", 20, 150.00),
    ("Escáneres de diagnóstico", "Autel MaxiCOM MK808", 17, 500.00),
    ("Herramientas de medición", "Fluke 87-V", 25, 400.00),
    ("Equipos de análisis de gases", "Bosch ETT 030", 16, 1500.00),
    ("Software de diagnóstico", "OBDLink MX+", 60, 100.00),
    ("Filtros de combustible", "K&N PF-2100", 35, 15.00),
    ("Masillas", "3M 01131", 50, 10.00),
    ("Pinturas automotrices", "Dupli-Color BSP200", 22, 20.00),
    ("Lijadoras", "DEWALT DWE6421K", 28, 70.00),
    ("Pistolas de pintura", "DeVilbiss 802342", 18, 150.00),
    ("Selladores", "Permatex 80019", 55, 5.00),
    ("Radiadores", "Spectra Premium CU1193", 25, 120.00),
    ("Bombas de agua", "Aisin WPT-190", 20, 50.00),
    ("Mangueras de refrigerante", "Gates 22437", 45, 12.00),
    ("Ventiladores de radiador", "Dorman 620-073", 19, 80.00),
    ("Baterías automotrices", "Optima 34/78 RedTop", 45, 200.00),
    ("Terminales de batería", "Schumacher BAF-BTC", 50, 8.00),
    ("Cables de batería", "ACDelco 4SD37XR", 30, 20.00),
    ("Cargadores de batería", "NOCO GENIUS10", 18, 100.00),
    ("Productos de limpieza de interiores", "Meguiar's G13616", 40, 10.00),
    ("Ceras y pulimentos", "Turtle Wax 53409", 30, 15.00),
    ("Esponjas y paños", "Chemical Guys MIC_292_02", 70, 5.00),
    ("Aspiradoras automotrices", "BLACK+DECKER BDH1200FVAV", 24, 40.00),
    ("Limpiadores de llantas", "Armor All 78011", 65, 8.00),
    ("Cables de bujía", "ACDelco 9718Q", 50, 25.00),
    ("Bobinas de encendido", "Delphi GN10328", 25, 35.00),
    ("Distribuidores", "Spectra Premium FD10", 20, 150.00),
    ("Módulos de encendido", "Standard Motor Products LX364", 18, 80.00),
    ("Bombas de combustible", "Bosch 67658", 22, 60.00),
    ("Inyectores de combustible", "Bosch 0280158821", 30, 50.00),
    ("Reguladores de presión de combustible", "Standard PR403", 17, 45.00),
    ("Tanques de combustible", "Dorman 576-121", 15, 250.00),
    ("Convertidores catalíticos", "MagnaFlow 27402", 35, 300.00),
    ("Reguladores de voltaje", "Standard VR166", 22, 25.00),
    ("Motores de ventilador", "TYC 700013", 19, 60.00),
    ("Resistencias del ventilador", "ACDelco 15-80521", 27, 20.00),
    ("Radiadores de calefacción", "Spectra Premium 93060", 18, 100.00),
    ("Controles de climatización", "Four Seasons 74627", 20, 150.00),
    ("Conductos de aire", "Dorman 258-5001", 22, 30.00)
]

for nombre, modelo, cantidad, costo in refacciones:
    x = Refacciones(nombre, modelo, cantidad, costo)
    session.add(x)

session.commit()

