import re

file_path = '/Users/davidestrella/PROYECTOS/webs/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# Define the new HeroSession content
new_hero_content = """        const HeroSession = ({ onNavigate }) => {
            const [scrollY, setScrollY] = useState(0);
            
            useEffect(() => {
                const handleScroll = () => setScrollY(window.scrollY);
                window.addEventListener('scroll', handleScroll, { passive: true });
                return () => window.removeEventListener('scroll', handleScroll);
            }, []);

            return (
                <header className="relative min-h-screen p-4 md:p-8 flex flex-col">
                    {/* Main Card Container - Liquid Glass Effect */}
                    <div className="relative flex-grow rounded-[3rem] overflow-hidden border border-white/20 shadow-[0_0_50px_rgba(30,58,138,0.3)] backdrop-blur-sm bg-white/5">
                        
                        {/* Background Image with Zoom */}
                        <div className="absolute inset-0 z-0 select-none">
                            <img
                                src="assets/hero-bg-v3.png"
                                className="w-full h-full object-cover opacity-80"
                                style={{ 
                                    transform: `scale(${1 + scrollY * 0.0005})`,
                                    transition: 'transform 0.1s linear',
                                    objectPosition: 'center 20%' 
                                }}
                                alt="STRELLA Background"
                            />
                            <div className="absolute inset-0 bg-gradient-to-t from-[#0a0a0a] via-transparent to-black/20"></div>
                            {/* Texture Overlay - Liquid feel */}
                            <div className="absolute inset-0 opacity-30 mix-blend-overlay bg-[url('https://www.transparenttextures.com/patterns/stardust.png')]"></div>
                        </div>

                        {/* Top Navigation Row (Inside Card) */}
                        <div className="absolute top-0 left-0 w-full p-8 md:p-12 z-20 flex justify-between items-start">
                             <div className="flex flex-col gap-1">
                                <span className="text-[10px] uppercase tracking-[0.3em] text-blue-300 font-bold drop-shadow-md">Social Media Design</span>
                                <span className="text-[10px] uppercase tracking-[0.3em] text-white/60">• Branding</span>
                             </div>
                             <div className="text-right hidden md:block">
                                <span className="text-[10px] uppercase tracking-[0.3em] text-white/60 block">Design that speaks.</span>
                                <span className="text-[10px] uppercase tracking-[0.3em] text-white/60 block">Visuals that convert.</span>
                             </div>
                        </div>

                        {/* Center Content */}
                        <div className="relative z-10 flex flex-col justify-center items-center h-full text-center mt-[-5vh]">
                            
                            {/* Giant Background Typography - Centered & Behind */}
                            <h1 
                                className="text-[22vw] leading-none font-black tracking-tighter text-white/10 absolute select-none pointer-events-none mix-blend-overlay blur-sm" 
                                style={{ fontFamily: "Inter, sans-serif", top: '50%', left: '50%', transform: 'translate(-50%, -50%)' }}
                            >
                                STRELLA
                            </h1>

                            {/* Main Foreground Content */}
                            <div className="relative animate-fade-in stagger-1 z-20">
                                <div className="mb-6 flex items-center justify-center gap-4">
                                     <span className="w-12 h-[1px] bg-[#1e3a8a] box-shadow-glow"></span>
                                     <span className="text-[#1e3a8a] uppercase tracking-[0.4em] text-xs font-bold drop-shadow-lg">Lens & Layers</span>
                                     <span className="w-12 h-[1px] bg-[#1e3a8a] box-shadow-glow"></span>
                                </div>
                                
                                <h2 className="text-6xl md:text-9xl font-serif italic text-white mb-2 tracking-tight drop-shadow-2xl">
                                    David Estrella
                                </h2>
                                <p className="text-xl md:text-2xl text-blue-100/80 font-light tracking-[0.2em] font-branding uppercase mb-12 drop-shadow-md">
                                    Filmmaker & Visual Artist
                                </p>

                                <div className="flex flex-col md:flex-row items-center justify-center gap-8">
                                    <button 
                                        onClick={() => onNavigate('works')}
                                        className="bg-[#1e3a8a] text-white px-10 py-4 rounded-full font-bold uppercase tracking-widest text-[10px] hover:bg-white hover:text-[#1e3a8a] transition-all shadow-[0_0_20px_rgba(30,58,138,0.5)] hover:shadow-[0_0_30px_rgba(255,255,255,0.4)] border border-white/10 backdrop-blur-md"
                                    >
                                        Ver Portafolio
                                    </button>
                                     <button
                                        onClick={() => onNavigate('contact')}
                                        className="text-white border-b border-[#1e3a8a]/50 pb-1 uppercase tracking-[0.3em] text-[10px] hover:border-blue-400 hover:text-blue-300 transition-all drop-shadow-md"
                                    >
                                        Reservar Fecha
                                    </button>
                                </div>
                            </div>
                        </div>

                        {/* Bottom Decoration */}
                        <div className="absolute bottom-12 left-0 w-full px-12 flex justify-between items-end z-20">
                            <div className="text-left">
                                <span className="block text-4xl font-serif italic text-white/30 drop-shadow-lg">Creative</span>
                                <span className="block text-[10px] uppercase tracking-widest text-blue-400">Visual Designer</span>
                            </div>
                           
                            {/* Scroll Indicator */}
                            <div className="animate-bounce">
                                <ChevronRight className="rotate-90 text-blue-300" />
                            </div>
                        </div>
                    </div>
                </header>
            );
        };"""

# Use regex to find the HeroSession block and replace it
# Pattern matches from "const HeroSession" up to the closing "};" before "const AboutSection"
pattern = r"const HeroSession = \(\{ onNavigate \}\) => \{[\s\S]*?\}\s*return \([\s\S]*?\);\s*\};"

# Find the start of HeroSession and end before AboutSection
start_marker = "const HeroSession = ({ onNavigate }) => {"
end_marker = "const AboutSection = () => ("

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # We found the block boundaries. Now we replace everything in between (inclusive of start, exclusive of end)
    # Actually, we want to replace the whole HeroSession function definition.
    # The end_idx is where AboutSection starts. We assume HeroSession ends just before it.
    
    # Let's verify what's before AboutSection. Usually closely following.
    # We will slice content[:start_idx] + new_hero_content + "\n\n        " + content[end_idx:]
    
    new_file_content = content[:start_idx] + new_hero_content + "\n\n        " + content[end_idx:]
    
    with open(file_path, 'w') as f:
        f.write(new_file_content)
    print("Successfully replaced HeroSession.")
else:
    print("Could not find HeroSession or AboutSection markers.")
