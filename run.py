import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        sys.stderr.write("%s - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format%args))

def find_available_port(start_port=8000, max_attempts=20):
    for port in range(start_port, start_port + max_attempts):
        try:
            with socketserver.TCPServer(("", port), QuietHandler) as s:
                return port
        except OSError:
            continue
    return start_port

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = find_available_port(PORT)
    url = f"http://localhost:{port}/index.html"

    print("=" * 64)
    print("  ★... 싸이월드 감성 가든 하우스 다이어트 미니홈피 ...★")
    print("  도토리(🌰) 모으고 미니룸 꾸미며 성공하는 즐거운 다이어트!")
    print("=" * 64)
    print(f"▶ 서버 주소: {url}")
    print("▶ 웹 브라우저가 자동으로 열립니다. (종료: Ctrl+C)")
    print("=" * 64)

    # 기본 웹브라우저 자동 열기
    webbrowser.open(url)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n다이어트 미니홈피를 안전하게 종료합니다. 퍼가요~♡")

if __name__ == "__main__":
    main()
