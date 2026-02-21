import re

file_path = '/Users/davidestrella/PROYECTOS/webs/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_components = """
        // --- GRADUACIONES HUB & GALLERY ---
        
        const StarryBackground = () => (
          <div className="absolute inset-0 overflow-hidden pointer-events-none opacity-60">
            <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <pattern id="stars" x="0" y="0" width="120" height="120" patternUnits="userSpaceOnUse">
                  <circle fill="#e2c779" cx="15" cy="15" r="1.5" opacity="0.8"/>
                  <circle fill="#e2c779" cx="50" cy="50" r="1" opacity="0.5"/>
                  <circle fill="#e2c779" cx="90" cy="20" r="2" opacity="0.9"/>
                  <circle fill="#e2c779" cx="30" cy="90" r="1.2" opacity="0.6"/>
                  <circle fill="#e2c779" cx="100" cy="95" r="1" opacity="0.4"/>
                  <circle fill="#e2c779" cx="70" cy="70" r="1.5" opacity="0.7"/>
                </pattern>
              </defs>
              <rect x="0" y="0" width="100%" height="100%" fill="url(#stars)" />
            </svg>
          </div>
        );

        const GraduationGalleryUNAP2026 = ({ onNavigate }) => {
          const CONFIG = {
            API_KEY: "AIzaSyDQtuaas4lv62ZSR79hQsRzuljxUZPc0Fg", 
            FOLDER_ID: "175b7qNGksPhNb0qYQbxhjNQu-9PvkvFe",
            EVENT_NAME: "Fiesta de Graduación",
          };

          const [photos, setPhotos] = useState([]);
          const [loading, setLoading] = useState(true);
          const [selectedPhoto, setSelectedPhoto] = useState(null);
          const [error, setError] = useState(null);

          useEffect(() => {
            const fetchPhotos = async () => {
              try {
                const query = encodeURIComponent(`'${CONFIG.FOLDER_ID}' in parents and mimeType contains 'image/' and trashed = false`);
                const fields = encodeURIComponent('files(id, name, webContentLink, thumbnailLink, mimeType)');
                const url = `https://www.googleapis.com/drive/v3/files?q=${query}&fields=${fields}&key=${CONFIG.API_KEY}`;

                const response = await fetch(url);
                if (!response.ok) throw new Error("No se pudo conectar a Google Drive. Verifica tu API Key o los permisos de la carpeta.");
                
                const data = await response.json();
                let optimizedFiles = [];

                if (data.files && data.files.length > 0) {
                  optimizedFiles = data.files.map(file => ({
                    ...file,
                    thumbnailLink: file.thumbnailLink ? file.thumbnailLink.replace('=s220', '=s1000') : null
                  }));
                  setPhotos(optimizedFiles);
                }
                setLoading(false);
              } catch (err) {
                console.error("Error al cargar fotos:", err);
                setError(err.message);
                setLoading(false);
              }
            };
            fetchPhotos();
            
            // Scroll to top when mounted
            window.scrollTo(0, 0);
          }, [CONFIG.API_KEY, CONFIG.FOLDER_ID]);

          const downloadPhoto = (url) => {
            if (!url) return;
            window.open(url, '_blank');
          };

          return (
            <div className="min-h-screen bg-[#f9f9f9] text-neutral-900 font-sans mt-20 md:mt-0 animate-fade-in relative z-10 w-full mb-0 pb-0 flex flex-col items-stretch">
              <style dangerouslySetInnerHTML={{__html: `
                @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&display=swap');
                .font-cinzel { font-family: 'Cinzel', serif; }
                .font-playfair { font-family: 'Playfair Display', serif; }
              `}} />

              {/* Botón de volver */}
              <button 
                onClick={() => onNavigate('graduaciones')}
                className="absolute top-6 left-6 z-50 bg-black/50 hover:bg-black text-white px-4 py-2 rounded-full backdrop-blur-md flex items-center gap-2 transition-all uppercase tracking-widest text-[10px]"
              >
                Volver
              </button>

              <header className="relative w-full min-h-[70vh] bg-[#151515] flex items-center justify-center overflow-hidden border-b-[6px] border-[#c5a059] py-20 px-4">
                <StarryBackground />
                <div className="absolute inset-0 bg-gradient-to-b from-transparent via-[#151515]/50 to-[#151515] pointer-events-none"></div>

                <div className="relative z-10 w-full max-w-5xl mx-auto flex flex-col items-center text-center mt-8">
                  <div className="hidden md:block absolute -top-8 right-4 text-center drop-shadow-lg">
                    <div className="text-[#e2c779] font-playfair italic text-5xl mb-1">31</div>
                    <div className="text-[#e2c779] font-playfair italic text-2xl tracking-wide">Enero</div>
                    <div className="text-[#e2c779] font-playfair italic text-2xl tracking-widest mt-1">2026</div>
                  </div>

                  <div className="relative mb-6">
                    <GraduationCap size={130} color="#c5a059" fill="#2d5a40" strokeWidth={1} className="drop-shadow-[0_15px_15px_rgba(0,0,0,0.8)] transform -rotate-3" />
                  </div>

                  <h1 className="text-[#e2c779] text-6xl md:text-8xl font-playfair italic drop-shadow-[0_4px_4px_rgba(0,0,0,0.5)] mb-6 leading-tight">
                    Fiesta de<br />Graduación
                  </h1>

                  <p className="text-[#c5a059] text-xs md:text-lg font-cinzel tracking-[0.2em] md:tracking-[0.3em] uppercase drop-shadow-md px-4 mt-2">
                    "Formados para cuidar, listos para liderar"
                  </p>

                  <div className="md:hidden mt-12 pt-6 border-t border-[#c5a059]/30 w-3/4 mx-auto">
                    <div className="text-[#e2c779] font-playfair italic text-3xl">31 Enero 2026</div>
                  </div>
                </div>
              </header>

              <main className="max-w-7xl mx-auto py-16 px-4 md:px-8 w-full flex-grow">
                <div className="text-center mb-12">
                  <h2 className="text-xl md:text-2xl font-cinzel text-neutral-800 tracking-widest uppercase mb-4">
                    Galería de Recuerdos
                  </h2>
                  <div className="h-px w-20 bg-[#c5a059] mx-auto"></div>
                </div>

                {loading ? (
                  <div className="flex flex-col items-center justify-center py-20 text-[#c5a059]">
                    <Loader2 className="animate-spin mb-4" size={40} strokeWidth={1.5} />
                    <p className="font-playfair italic text-lg text-neutral-500">Preparando la galería...</p>
                  </div>
                ) : error ? (
                  <div className="max-w-md mx-auto text-center py-20 px-6 bg-white border border-red-100 rounded-lg shadow-sm">
                    <AlertCircle className="mx-auto mb-4 text-red-400" size={48} />
                    <h2 className="text-lg font-medium text-neutral-800 mb-2">Aviso</h2>
                    <p className="text-sm text-neutral-500 mb-6">{error}</p>
                  </div>
                ) : photos.length === 0 ? (
                  <div className="text-center py-20 text-neutral-400">
                    <ImageIcon className="mx-auto mb-4 opacity-20" size={64} />
                    <p className="font-playfair italic text-xl text-neutral-600 mb-2">Aún no hay fotos disponibles.</p>
                    <p className="text-sm text-neutral-500">Las imágenes aparecerán aquí automáticamente una vez que se suban a tu carpeta de Drive.</p>
                  </div>
                ) : (
                  <div className="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6">
                    {photos.map((photo) => (
                      <div key={photo.id} className="relative group overflow-hidden bg-neutral-100 break-inside-avoid shadow-sm hover:shadow-2xl transition-all duration-700 rounded-sm">
                        <img 
                          src={photo.thumbnailLink || 'https://via.placeholder.com/800x600?text=Cargando...'} 
                          alt={photo.name}
                          className="w-full h-auto object-cover transition-transform duration-1000 group-hover:scale-105 cursor-pointer"
                          onClick={() => setSelectedPhoto(photo)}
                        />
                        <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-6">
                          <div className="flex justify-between items-center transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                            <button onClick={() => setSelectedPhoto(photo)} className="flex items-center gap-2 text-[#e2c779] text-xs tracking-widest uppercase font-cinzel">
                              <ZoomIn size={18} strokeWidth={2} /> Ver
                            </button>
                            <button onClick={() => downloadPhoto(photo.webContentLink)} className="p-3 bg-[#c5a059] text-white rounded-full hover:bg-[#b08d4a] transition-colors shadow-lg" title="Descargar Original">
                              <Download size={18} />
                            </button>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </main>

              {selectedPhoto && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/95 backdrop-blur-sm p-4 md:p-8 animate-in fade-in duration-200">
                  <button onClick={() => setSelectedPhoto(null)} className="absolute top-6 right-6 p-2 text-white/50 hover:text-white transition-colors z-[60]">
                    <X size={36} strokeWidth={1} />
                  </button>
                  <div className="max-w-7xl w-full h-full flex flex-col items-center justify-center gap-6 relative z-50">
                    <div className="relative flex-1 flex items-center justify-center overflow-hidden w-full h-[80vh]">
                      <img src={selectedPhoto.thumbnailLink} alt={selectedPhoto.name} className="max-h-full max-w-full object-contain shadow-2xl rounded-sm" />
                    </div>
                    <div className="flex flex-col items-center gap-4 pb-2">
                      <button onClick={() => downloadPhoto(selectedPhoto.webContentLink)} className="flex items-center gap-3 px-8 py-3 bg-[#c5a059] text-white hover:bg-[#b08d4a] transition-all tracking-widest uppercase text-xs font-cinzel rounded-sm shadow-[0_0_15px_rgba(197,160,89,0.3)] hover:shadow-[0_0_25px_rgba(197,160,89,0.5)] active:scale-95">
                        <Download size={18} /> Descargar en Alta Calidad
                      </button>
                    </div>
                  </div>
                </div>
              )}

              <footer className="py-16 px-6 text-center border-t border-neutral-200 bg-[#151515] text-[#e2c779] w-full mt-auto">
                <div className="max-w-xs mx-auto mb-6 h-px bg-[#c5a059]/30"></div>
                <p className="text-[10px] uppercase tracking-[0.3em] mb-3 text-[#e2c779]/70 font-cinzel">UNAP • Promoción 2026</p>
                <p className="text-xs font-light text-[#e2c779]/50 font-playfair italic">"Formados para cuidar, listos para liderar"</p>
              </footer>
            </div>
          );
        };

        const GraduacionesSection = ({ onNavigate }) => {
            const galleries = [
                { 
                    id: 'graduacion-unap-2026',
                    title: "Promoción 2026",
                    subtitle: "UNAP Enfermería", 
                    date: "Enero 2026",
                    size: "item-tall", 
                    img: "https://images.unsplash.com/photo-1523580494863-6f3031224c94?q=80&w=2070",
                    accent: "from-[#2d5a40]/60" // verde enfermeria
                },
                // Futuros eventos irían aquí
            ];

            return (
                <section className="py-32 bg-stone-950 min-h-screen text-white pt-48">
                    <div className="container mx-auto px-6">
                        <button 
                            onClick={() => onNavigate('trabajos')}
                            className="bg-white/5 hover:bg-white/10 text-white px-4 py-2 mb-12 rounded-full flex items-center gap-2 transition-all uppercase tracking-widest text-[10px] border border-white/10"
                        >
                            <X size={14} className="rotate-45" /> Volver a Trabajos
                        </button>
                        
                        <div className="text-center mb-24">
                            <span className="text-[#c5a059] uppercase tracking-[0.4em] text-xs mb-6 block font-bold">Portafolio</span>
                            <h2 className="text-4xl md:text-6xl font-branding uppercase tracking-widest mb-6 border-b border-white/10 inline-block pb-4">Graduaciones</h2>
                            <p className="text-stone-500 max-w-2xl mx-auto text-lg font-light">Accede a las galerías privadas de los eventos.</p>
                        </div>

                        <div className="bento-grid">
                            {galleries.map((gal, i) => (
                                <div key={i} onClick={() => onNavigate(gal.id)} className={`bento-item ${gal.size} group cursor-pointer border border-[#c5a059]/20 hover:border-[#c5a059]/50 relative overflow-hidden`} style={{minHeight: '400px'}}>
                                    <img src={gal.img} alt={gal.title} className="absolute inset-0 w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110" />
                                    <div className={`absolute inset-0 bg-gradient-to-t ${gal.accent} via-black/50 to-transparent opacity-90 transition-opacity`}></div>
                                    
                                    <div className="absolute inset-0 flex flex-col justify-end p-8 z-10">
                                        <span className="text-[#c5a059] font-playfair italic text-lg mb-2">{gal.date}</span>
                                        <h3 className="text-3xl md:text-4xl font-branding uppercase tracking-widest text-white mb-2">{gal.title}</h3>
                                        <p className="text-white/70 font-cinzel text-sm uppercase tracking-widest">{gal.subtitle}</p>
                                    </div>
                                    <div className="absolute top-6 right-6">
                                        <div className="w-12 h-12 rounded-full border border-white/30 flex items-center justify-center backdrop-blur-sm bg-black/30 group-hover:bg-[#c5a059] pointer-events-none transition-colors">
                                            <ArrowUpRight size={20} className="text-white" />
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>
            );
        };
"""

content = content.replace('        const TrabajosSection = () => {', new_components + '\n        const TrabajosSection = ({ onNavigate }) => {')

content = content.replace(
    'case \'trabajos\': return <TrabajosSection />;',
    "case 'trabajos': return <TrabajosSection onNavigate={setSection} />;\n                    case 'graduaciones': return <GraduacionesSection onNavigate={setSection} />;\n                    case 'graduacion-unap-2026': return <GraduationGalleryUNAP2026 onNavigate={setSection} />;"
)

# Also update the hardcoded TrabajosSection item to click through to graduaciones
# I'll find 'title: "Bodas"' and go to Graduaciones item.
# But it's easier to regex replace just the Graduaciones div if it was a plain text, but it's generated via map.
# So I'll modify TrabajosSection map explicitly to handle `onClick`.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected components.")
