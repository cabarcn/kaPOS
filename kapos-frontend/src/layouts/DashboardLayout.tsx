// src/layouts/DashboardLayout.tsx
import { Link, useNavigate } from "react-router-dom";

type DashboardLayoutProps = {
  children: React.ReactNode;
};

export default function DashboardLayout({ children }: DashboardLayoutProps) {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("kapos_access");
    localStorage.removeItem("kapos_refresh");
    localStorage.removeItem("kapos_user");
    navigate("/login");
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        background: "#020617", // fondo oscuro
        color: "#e5e7eb",
        fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif",
      }}
    >
      {/* SIDEBAR */}
      <aside
        style={{
          width: "260px",
          padding: "1.5rem",
          borderRight: "1px solid rgba(148, 163, 184, 0.3)",
          background:
            "radial-gradient(circle at top, rgba(56,189,248,0.2), transparent 60%), radial-gradient(circle at bottom, rgba(52,211,153,0.15), transparent 55%), #020617",
          display: "flex",
          flexDirection: "column",
          gap: "1.5rem",
        }}
      >
        <div>
          <h2
            style={{
              fontSize: "1.2rem",
              fontWeight: 700,
              marginBottom: "0.15rem",
            }}
          >
            KAPOS Admin
          </h2>
          <p
            style={{
              fontSize: "0.75rem",
              textTransform: "uppercase",
              letterSpacing: "0.16em",
              color: "#9ca3af",
            }}
          >
            Control Center
          </p>
        </div>

        {/* NAV */}
        <nav
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "0.75rem",
            fontSize: "0.9rem",
          }}
        >
          <NavLink to="/dashboard" label="Inicio" />
          <NavLink to="/clientes" label="Clientes" />
          <NavLink to="/planes" label="Planes" />
          <NavLink to="/suscripciones" label="Suscripciones" />
        </nav>

        <button
          onClick={logout}
          style={{
            marginTop: "auto",
            padding: "0.55rem 0.75rem",
            borderRadius: "9999px",
            border: "1px solid rgba(248,113,113,0.6)",
            background: "transparent",
            color: "#fecaca",
            fontSize: "0.85rem",
            cursor: "pointer",
          }}
        >
          Cerrar sesión
        </button>
      </aside>

      {/* CONTENIDO PRINCIPAL */}
      <main
        style={{
          flex: 1,
          padding: "2rem 2.5rem",
          display: "flex",
          flexDirection: "column",
          gap: "1.5rem",
          background:
            "radial-gradient(circle at top left, rgba(59,130,246,0.18), transparent 55%), radial-gradient(circle at bottom right, rgba(45,212,191,0.16), transparent 55%), #020617",
        }}
      >
        {children}
      </main>
    </div>
  );
}

type NavLinkProps = {
  to: string;
  label: string;
};

function NavLink({ to, label }: NavLinkProps) {
  return (
    <Link
      to={to}
      style={{
        textDecoration: "none",
        color: "#cbd5f5",
        padding: "0.4rem 0.75rem",
        borderRadius: "9999px",
        border: "1px solid transparent",
        fontSize: "0.9rem",
      }}
      onMouseEnter={(e) => {
        (e.currentTarget as HTMLAnchorElement).style.background =
          "rgba(15,23,42,0.9)";
        (e.currentTarget as HTMLAnchorElement).style.borderColor =
          "rgba(148,163,184,0.7)";
      }}
      onMouseLeave={(e) => {
        (e.currentTarget as HTMLAnchorElement).style.background = "transparent";
        (e.currentTarget as HTMLAnchorElement).style.borderColor =
          "transparent";
      }}
    >
      {label}
    </Link>
  );
}
