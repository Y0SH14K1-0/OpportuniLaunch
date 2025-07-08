#!/usr/bin/env python3
"""
Simple HTTP server for the Opportuni landing page with health check support.
Optimized for deployment on Replit and Cloud Run.
"""

import http.server
import socketserver
import os
import sys
from urllib.parse import urlparse

class OpportuniHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with health check support."""
    
    def do_GET(self):
        """Handle GET requests with health check support."""
        # Parse the URL
        parsed_path = urlparse(self.path)
        
        # Health check endpoint for deployment systems
        if parsed_path.path == '/health' or parsed_path.path == '/healthz':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
            return
        
        # Default behavior for all other requests
        super().do_GET()
    
    def log_message(self, format, *args):
        """Override to provide cleaner logging."""
        print(f"[{self.address_string()}] {format % args}")

def run_server(port=5000, bind_address='0.0.0.0'):
    """Run the HTTP server."""
    try:
        # Allow socket reuse to avoid "Address already in use" errors
        socketserver.TCPServer.allow_reuse_address = True
        
        with socketserver.TCPServer((bind_address, port), OpportuniHTTPRequestHandler) as httpd:
            print(f"Serving Opportuni landing page on {bind_address}:{port}")
            print(f"Health check available at: http://{bind_address}:{port}/health")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Port {port} is already in use. Trying to find alternative port...")
            # Try a few alternative ports
            for alt_port in range(port + 1, port + 10):
                try:
                    with socketserver.TCPServer((bind_address, alt_port), OpportuniHTTPRequestHandler) as httpd:
                        print(f"Serving Opportuni landing page on {bind_address}:{alt_port}")
                        print(f"Health check available at: http://{bind_address}:{alt_port}/health")
                        httpd.serve_forever()
                        break
                except OSError:
                    continue
            else:
                print(f"Could not find available port. Error: {e}")
                sys.exit(1)
        else:
            print(f"Error starting server: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 5000))
    
    # Always bind to 0.0.0.0 for deployment compatibility
    bind_address = '0.0.0.0'
    
    print(f"Starting Opportuni server...")
    run_server(port, bind_address)