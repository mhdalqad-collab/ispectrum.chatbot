import "./globals.css";

export const metadata = {
  title: "iSpectrum",
  description: "Chat Assistant",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <div className="container">
          <header className="header">
            <div className="brand">
              <span className="logo" />
              <span>iSpectrum</span>
            </div>
          </header>

          <main className="main">{children}</main>

          <footer className="footer">
            © {new Date().getFullYear()} iSpectrum
          </footer>
        </div>
      </body>
    </html>
  );
}