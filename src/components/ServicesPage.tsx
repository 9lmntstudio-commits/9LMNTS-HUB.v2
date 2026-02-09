import { Mic2, Disc3, Paintbrush, Users, Radio, BookOpen, Lightbulb, Code, Palette, Brain, Zap, Globe, TrendingUp, Target, DollarSign } from 'lucide-react';
import { ImageWithFallback } from './figma/ImageWithFallback';

interface ServicesPageProps {
  onNavigate: (page: string, plan?: string) => void;
}

export function ServicesPage({ onNavigate }: ServicesPageProps) {
  const tiers = [
    {
      name: 'EventOS Basic Boost',
      price: '$1,500 CAD',
      value: 'basic',
      description: 'EventOS Platform License with basic features',
      icon: Zap,
      features: ['Initial Concept', '1 Revision Round', 'Basic Mockups', 'Mobile Responsive'],
      image: 'https://images.unsplash.com/photo-1730463527127-7c6c1c1faf6d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtaWNyb3Bob25lJTIwcmFwcGVyJTIwc3R1ZGlvfGVufDF8fHx8MTc2NDcxODYyM3ww&ixlib=rb-4.1.0&q=80&w=1080'
    },
    {
      name: 'EventOS Standard Pro',
      price: '$3,000 CAD',
      value: 'standard',
      description: 'EventOS + AI Event Operator + Analytics',
      icon: Zap,
      features: ['Full Wireframe', '2 Revision Rounds', 'Interactive Prototype', 'Analytics'],
      image: 'https://images.unsplash.com/photo-1600542552868-56ed242290e7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxESiUyMHR1cm50YWJsZSUyMG1peGluZyUyMGRhdGFiYXNlfGVufDF8fHx8MTc2NDcxODYyNHww&ixlib=rb-4.1.0&q=80&w=1080'
    },
    {
      name: 'EventOS Premium Elite',
      price: '$5,000 CAD',
      value: 'premium',
      description: 'EventOS + AI + White-label Rights',
      icon: Palette,
      features: ['Full UX Research', 'Unlimited Revisions', 'White-label rights', 'Advanced AI'],
      image: 'https://images.unsplash.com/photo-1628522994788-53bc1b1502c5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxncmFmZml0aSUyMHN0cmVldCUyMGFydHxlbnwxfHx8fDE3NjQ4MzQ0NDR8MA&ixlib=rb-4.1.0&q=80&w=1080'
    },
    {
      name: 'EventOS Custom Scale',
      price: 'Custom Pricing',
      value: 'custom',
      description: 'Enterprise solutions with custom features',
      icon: Globe,
      features: ['Dedicated Team', 'Custom Timeline', 'White Label Solutions', '24/7 Support'],
      image: 'https://images.unsplash.com/photo-1540397106260-e24a507a08ea?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxzdGFydHVwJTIwY29kaW5nJTIwd29ya3NwYWNlfGVufDF8fHx8MTc2NDcxODYyNnww&ixlib=rb-4.1.0&q=80&w=1080'
    }
  ];

  return (
    <div className="min-h-screen bg-[#1A1A1A] pt-16">
      {/* Hero Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-6xl mx-auto text-center">
          <div className="mb-6">
            <span className="px-4 py-2 bg-[#222222] border border-[#FF7A00]/30 rounded-full text-[#FF7A00] text-sm">
              EventOS Licensing
            </span>
          </div>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl text-white mb-6">
            <span className="font-futuristic">Choose Your</span><br />
            <span className="font-graffiti text-[#FF7A00]">EventOS Tier</span>
          </h1>
          <p className="text-lg sm:text-xl text-gray-400 max-w-3xl mx-auto">
            Select the perfect licensing tier for your event platform.
            All plans include our signature AI-driven EventOS core.
          </p>
        </div>
      </section>

      {/* Services Grid */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-[#0D0D0D]">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {tiers.map((tier, index) => {
              const Icon = tier.icon || Zap;
              return (
                <div
                  key={index}
                  onClick={() => onNavigate('start-project', tier.value)}
                  className="group bg-[#222222] rounded-lg border border-[#FF7A00]/20 hover:border-[#FF7A00] transition-all hover:transform hover:scale-105 cursor-pointer overflow-hidden flex flex-col"
                >
                  {/* Image Section */}
                  <div className="relative h-48 overflow-hidden">
                    <ImageWithFallback
                      src={tier.image}
                      alt={tier.name}
                      className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-[#222222] via-[#222222]/50 to-transparent"></div>

                    {/* Icon Overlay */}
                    <div className="absolute top-4 right-4 p-3 bg-[#FF7A00] rounded-lg group-hover:scale-110 transition-transform">
                      <Icon className="text-[#1A1A1A]" size={24} />
                    </div>
                  </div>

                  {/* Content Section */}
                  <div className="p-6 flex flex-col flex-1">
                    <h3 className="text-white text-xl mb-3 group-hover:text-[#FF7A00] transition-colors">
                      {tier.name}
                    </h3>
                    <p className="text-gray-400 text-sm mb-4 leading-relaxed flex-1">
                      {tier.description}
                    </p>
                    <div className="mb-4">
                      <span className="text-[#FF7A00] font-bold text-2xl">{tier.price}</span>
                    </div>
                    <div>
                      <div className="flex flex-wrap gap-2">
                        {tier.features.map((feature, featureIndex) => (
                          <span key={featureIndex} className="px-2 py-1 bg-[#222222] border border-[#FF7A00]/20 rounded text-[10px] text-gray-300">
                            {feature}
                          </span>
                        ))}
                      </div>
                    </div>
                    <button
                      className="mt-6 w-full py-3 bg-[#FF7A00] text-[#1A1A1A] font-bold rounded hover:bg-[#FF7A00]/90 transition-all opacity-0 group-hover:opacity-100"
                    >
                      Select Plan
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Process Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-[#0D0D0D]">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl sm:text-5xl text-white mb-4">
              <span className="font-futuristic">Our</span> <span className="font-graffiti text-[#FF7A00]">AI Sales Process</span>
            </h2>
            <p className="text-gray-400 text-lg">
              Automated lead generation, qualification, and closing - 24/7
            </p>
          </div>

          <div className="grid md:grid-cols-4 gap-8">
            {[
              { step: '01', title: 'AI Lead Scraping', desc: '24/7 automated lead generation and qualification' },
              { step: '02', title: 'AI Proposal Generation', desc: 'Instant AI-powered proposals and pricing' },
              { step: '03', title: 'AI Service Delivery', desc: 'Automated setup and deployment of AI services' },
              { step: '04', title: 'Revenue Collection', desc: 'Automated invoicing and payment processing' },
            ].map((phase, index) => (
              <div key={index} className="relative">
                <div className="text-6xl text-[#FF7A00]/20 mb-4">{phase.step}</div>
                <h3 className="text-white text-xl mb-2">{phase.title}</h3>
                <p className="text-gray-400">{phase.desc}</p>
                {index < 3 && (
                  <div className="hidden md:block absolute top-8 -right-4 w-8 h-0.5 bg-[#FF7A00]/30"></div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl sm:text-5xl text-white mb-6">
            <span className="font-futuristic">Ready to Build Your</span><br />
            <span className="font-graffiti text-[#FF7A00]">AI Empire?</span>
          </h2>
          <p className="text-gray-400 text-lg mb-8">
            Let's transform your business with Nine Pillars AI services and start generating revenue immediately
          </p>
          <button
            onClick={() => onNavigate('start-project')}
            className="px-8 py-4 bg-[#FF7A00] text-[#1A1A1A] rounded-lg hover:bg-[#FF7A00]/90 transition-all transform hover:scale-105"
          >
            Start Your AI Transformation
          </button>
        </div>
      </section>
    </div>
  );
}