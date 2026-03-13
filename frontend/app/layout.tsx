import "./globals.css";
import Image from "next/image";

export const metadata = {
  title: "Intelligent Spectrum",
  description: "AI Chat Assistant by Intelligent Spectrum",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <div className="container">
          <header className="header">
            <div className="brand">
              <Image
                src="Public/ILogo.png"
                alt="Intelligent Spectrum"
                width={36}
                height={36}
              />
              <span>Intelligent Spectrum</span>
            </div>
          </header>

          <main className="main">{children}</main>

          <footer className="footer">
            © {new Date().getFullYear()} Intelligent Spectrum
          </footer>
        </div>
      </body>
    </html>
  );
}
