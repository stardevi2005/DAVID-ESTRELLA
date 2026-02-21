import re
import os

file_path = '/Users/davidestrella/PROYECTOS/webs/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the original component
start_marker = "const GraduationGalleryUNAP2026 = ({ onNavigate }) => {"
end_marker = "const GraduacionesSection = ({ onNavigate }) => {"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers.")
    exit(1)

original_component = content[start_idx:end_idx]

# 2. Modify it to create the new component
new_component = original_component.replace(
    "const GraduationGalleryUNAP2026", "const CeremonyGalleryUNAP2026"
).replace(
    'FOLDER_ID: "175b7qNGksPhNb0qYQbxhjNQu-9PvkvFe"', 
    'FOLDER_ID: "1-pEcrb-lpVU0wFp8WuoS48_Y8izPqLDR"'
).replace(
    'EVENT_NAME: "Fiesta de Graduación"',
    'EVENT_NAME: "Ceremonia de Graduación"'
).replace(
    'Fiesta de<br />Graduación',
    'Ceremonia de<br />Graduación'
)

# 3. Inject it back into the content just before GraduacionesSection
content = content[:end_idx] + new_component + "        " + content[end_idx:]

# 4. Modify GraduacionesSection to include the new card
new_card = """                {
                    id: 'ceremonia-unap-2026',
                    title: "Ceremonia de Graduación",
                    subtitle: "Enfermería UNAP 2026",
                    date: "Enero 2026",
                    img: "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=2070",
                    accent: "from-[#2d5a40]/60" // verde enfermeria
                },
"""
card_insertion_idx = content.find("// Futuros eventos irían aquí")
if card_insertion_idx != -1:
    content = content[:card_insertion_idx] + new_card + "                " + content[card_insertion_idx:]
else:
    print("Could not find 'Futuros eventos irían aquí'")

# 5. Modify App router
router_marker = "case 'graduacion-unap-2026': return <GraduationGalleryUNAP2026 onNavigate={setSection} />;"
router_new = router_marker + "\n                    case 'ceremonia-unap-2026': return <CeremonyGalleryUNAP2026 onNavigate={setSection} />;"
content = content.replace(router_marker, router_new)

# 6. Modify validSections
valid_marker = "const validSections = ['home', 'sobre-mi', 'servicios', 'trabajos', 'contacto', 'graduaciones', 'graduacion-unap-2026'];"
valid_new = "const validSections = ['home', 'sobre-mi', 'servicios', 'trabajos', 'contacto', 'graduaciones', 'graduacion-unap-2026', 'ceremonia-unap-2026'];"
content = content.replace(valid_marker, valid_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Ceremony component injected successfully.")
