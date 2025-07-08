# Opportuni Landing Page

## Overview

Opportuni is a static landing page built to connect Latin American youth (ages 18-29) with educational and professional opportunities. The platform serves as a bridge between talented young people and various opportunities including scholarships, job vacancies, challenges, and programs. The landing page focuses on directing users to WhatsApp communities for Mexico and Colombia.

## System Architecture

This is a simple, static website architecture consisting of:

- **Frontend**: Pure HTML5, CSS3, and minimal JavaScript (if needed)
- **Hosting**: Static file hosting (suitable for platforms like GitHub Pages, Netlify, or Replit)
- **External Integration**: WhatsApp community links for user onboarding

### Technology Stack
- HTML5 for semantic structure
- CSS3 with modern features (CSS Grid, Flexbox, CSS Variables)
- Google Fonts (Poppins) for typography
- Font Awesome for iconography
- SVG graphics for illustrations and map visualization

## Key Components

### 1. Hero Section
- **Purpose**: Primary call-to-action with visual appeal
- **Features**: 
  - Animated LATAM map with country markers (Mexico 🇲🇽 and Colombia 🇨🇴)
  - Gradient background with pink-orange-yellow color scheme
  - Two prominent CTA buttons for WhatsApp communities
- **Design Decision**: Visual-first approach to immediately communicate the platform's regional focus

### 2. Manifesto Section
- **Purpose**: Explain the platform's mission and value proposition
- **Approach**: Emotional storytelling to connect with target demographic
- **Content**: Addresses the opportunity gap problem in Latin America

### 3. How It Works Section
- **Purpose**: User onboarding flow explanation
- **Structure**: 3-step process with visual icons
- **Steps**: Join → Choose sub-community → Share & Connect

### 4. Testimonials Section
- **Purpose**: Social proof and credibility
- **Layout**: 4-card grid system
- **Geographic Representation**: Stories from Mexico (Guadalajara, CDMX) and Colombia (Bogotá, Medellín)

### 5. Footer Section
- **Purpose**: Secondary CTAs and social media presence
- **Elements**: Community tagline, repeat WhatsApp buttons, social media links

## Data Flow

Since this is a static landing page, the data flow is minimal:

1. **User visits page** → Static HTML/CSS loads
2. **User clicks WhatsApp buttons** → External redirect to WhatsApp communities
3. **User clicks social media links** → External redirect to social platforms

No user data is collected or processed on the website itself.

## External Dependencies

### Required External Services
- **Google Fonts**: Poppins font family loading
- **Font Awesome CDN**: Icon library for UI elements
- **WhatsApp Web**: Community link destinations

### Optional External Services
- **Instagram**: Social media integration (@opportuni_mx)
- **LinkedIn**: Placeholder for future social media presence

## Deployment Strategy

### Current Setup
- Custom Python HTTP server with health check endpoint
- Static file hosting compatible
- No server-side processing required
- No database requirements
- CDN-friendly for global content delivery
- Deployment-ready with proper port binding (0.0.0.0:5000)
- Health check endpoint available at `/health` and `/healthz`

### Recommended Hosting Platforms
1. **Replit**: Direct deployment from development environment
2. **Netlify**: Automatic deployments with form handling capabilities
3. **GitHub Pages**: Free hosting with version control integration
4. **Vercel**: Fast global CDN with excellent performance

### Performance Considerations
- Minimal external dependencies to ensure fast loading
- SVG graphics for scalable illustrations
- CSS optimization for mobile responsiveness
- Font loading optimization with preconnect headers

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- July 08, 2025. Fixed deployment issues by creating custom Python server with health check endpoint
- July 02, 2025. Initial setup