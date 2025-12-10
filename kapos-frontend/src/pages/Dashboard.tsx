// src/pages/Dashboard.tsx
import { Link } from "react-router-dom";
import DashboardLayout from "../layouts/DashboardLayout";

const cardBaseStyle: React.CSSProperties = {
  position: "relative",
  overflow: "hidden",
  borderRadius: "18px",
  padding: "1.25rem 1.4rem",
  border: "1px solid rgba(148,163,184,0.4)",
  background:
    "linear-gradient(135deg, rgba(15,23,42,0.96), rgba(15,23,42,0.85))",
  boxShadow: "0 18px 30px rgba(0,0,0,0.55)",
};

export default function DashboardPage() {
  return (
    <DashboardLayout>
      <div style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
        {/* ENCABEZADO */}
        <section
          style={{
            display: "flex",
            flexWrap: "wrap",
            alignItems: "flex-start",
            justifyContent: "space-between",
            gap: "1.5rem",
          }}
        >
          <div>
            <p
              style={{
                fontSize: "0.7rem",
                textTransform: "uppercase",
                letterSpacing: "0.25em",
                color: "rgba(52,211,153,0.8)",
                marginBottom: "0.25rem",
              }}
            >
              Panel administrativo
            </p>
            <h1
              style={{
                fontSize: "2.4rem",
                fontWeight: 700,
                margin: 0,
              }}
            >
              KAPOS Control Center
            </h1>
            <p
              style={{
                marginTop: "0.6rem",
                maxWidth: "34rem",
                fontSize: "0.95rem",
                color: "#9ca3af",
              }}
            >
              Monitorea clientes, planes y suscripciones desde un panel claro,
              moderno y alineado al acceso de KAPos Panel.
            </p>
          </div>

          {/* KPIs RÁPIDOS */}
          <div
            style={{
              display: "flex",
              gap: "0.85rem",
              minWidth: "220px",
            }}
          >
            <div
              style={{
                ...cardBaseStyle,
                padding: "0.8rem 1rem",
                flex: 1,
              }}
            >
              <p
                style={{
                  fontSize: "0.7rem",
                  textTransform: "uppercase",
                  letterSpacing: "0.12em",
                  color: "#9ca3af",
                }}
              >
                Clientes activos
              </p>
              <p
                style={{
                  marginTop: "0.15rem",
                  fontSize: "1.4rem",
                  fontWeight: 600,
                  color: "#4ade80",
                }}
              >
                24
              </p>
            </div>

            <div
              style={{
                ...cardBaseStyle,
                padding: "0.8rem 1rem",
                flex: 1,
              }}
            >
              <p
                style={{
                  fontSize: "0.7rem",
                  textTransform: "uppercase",
                  letterSpacing: "0.12em",
                  color: "#9ca3af",
                }}
              >
                Suscripciones
              </p>
              <p
                style={{
                  marginTop: "0.15rem",
                  fontSize: "1.4rem",
                  fontWeight: 600,
                  color: "#38bdf8",
                }}
              >
                56
              </p>
            </div>
          </div>
        </section>

        {/* TARJETAS PRINCIPALES */}
        <section
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(230px, 1fr))",
            gap: "1.25rem",
          }}
        >
          {/* Clientes */}
          <article style={cardBaseStyle}>
            <div
              style={{
                position: "absolute",
                inset: 0,
                background:
                  "radial-gradient(circle at top left, rgba(34,197,94,0.22), transparent 55%)",
                opacity: 0.3,
                pointerEvents: "none",
              }}
            />
            <div style={{ position: "relative" }}>
              <h3
                style={{
                  fontSize: "1.1rem",
                  fontWeight: 600,
                  display: "flex",
                  alignItems: "center",
                  gap: "0.4rem",
                  marginBottom: "0.45rem",
                }}
              >
                Clientes
                <span
                  style={{
                    fontSize: "0.6rem",
                    textTransform: "uppercase",
                    letterSpacing: "0.12em",
                    color: "#4ade80",
                    background: "rgba(22,163,74,0.18)",
                    padding: "0.18rem 0.5rem",
                    borderRadius: "9999px",
                  }}
                >
                  Gestión
                </span>
              </h3>
              <p
                style={{
                  fontSize: "0.85rem",
                  color: "#9ca3af",
                  marginBottom: "0.7rem",
                }}
              >
                Revisa y administra el listado de organizaciones y contactos
                asociados a Kapos.
              </p>
              <Link
                to="/clientes"
                style={{
                  fontSize: "0.85rem",
                  fontWeight: 500,
                  color: "#4ade80",
                  textDecoration: "none",
                }}
              >
                Ver clientes →
              </Link>
            </div>
          </article>

          {/* Planes */}
          <article style={cardBaseStyle}>
            <div
              style={{
                position: "absolute",
                inset: 0,
                background:
                  "radial-gradient(circle at top right, rgba(56,189,248,0.22), transparent 55%)",
                opacity: 0.3,
                pointerEvents: "none",
              }}
            />
            <div style={{ position: "relative" }}>
              <h3
                style={{
                  fontSize: "1.1rem",
                  fontWeight: 600,
                  display: "flex",
                  alignItems: "center",
                  gap: "0.4rem",
                  marginBottom: "0.45rem",
                }}
              >
                Planes
                <span
                  style={{
                    fontSize: "0.6rem",
                    textTransform: "uppercase",
                    letterSpacing: "0.12em",
                    color: "#38bdf8",
                    background: "rgba(56,189,248,0.16)",
                    padding: "0.18rem 0.5rem",
                    borderRadius: "9999px",
                  }}
                >
                  Configuración
                </span>
              </h3>
              <p
                style={{
                  fontSize: "0.85rem",
                  color: "#9ca3af",
                  marginBottom: "0.7rem",
                }}
              >
                Define, actualiza y monitorea los planes disponibles para las
                organizaciones.
              </p>
              <Link
                to="/planes"
                style={{
                  fontSize: "0.85rem",
                  fontWeight: 500,
                  color: "#38bdf8",
                  textDecoration: "none",
                }}
              >
                Ver planes →
              </Link>
            </div>
          </article>

          {/* Suscripciones */}
          <article style={cardBaseStyle}>
            <div
              style={{
                position: "absolute",
                inset: 0,
                background:
                  "radial-gradient(circle at bottom, rgba(129,140,248,0.28), transparent 55%)",
                opacity: 0.3,
                pointerEvents: "none",
              }}
            />
            <div style={{ position: "relative" }}>
              <h3
                style={{
                  fontSize: "1.1rem",
                  fontWeight: 600,
                  display: "flex",
                  alignItems: "center",
                  gap: "0.4rem",
                  marginBottom: "0.45rem",
                }}
              >
                Suscripciones
                <span
                  style={{
                    fontSize: "0.6rem",
                    textTransform: "uppercase",
                    letterSpacing: "0.12em",
                    color: "#a855f7",
                    background: "rgba(168,85,247,0.18)",
                    padding: "0.18rem 0.5rem",
                    borderRadius: "9999px",
                  }}
                >
                  Monitoreo
                </span>
              </h3>
              <p
                style={{
                  fontSize: "0.85rem",
                  color: "#9ca3af",
                  marginBottom: "0.7rem",
                }}
              >
                Controla el estado de las suscripciones, renovaciones y
                cancelaciones.
              </p>
              <Link
                to="/suscripciones"
                style={{
                  fontSize: "0.85rem",
                  fontWeight: 500,
                  color: "#a855f7",
                  textDecoration: "none",
                }}
              >
                Ver suscripciones →
              </Link>
            </div>
          </article>
        </section>

        {/* SECCIÓN INFERIOR */}
        <section
          style={{
            display: "grid",
            gridTemplateColumns: "minmax(0,1.2fr) minmax(0,1fr)",
            gap: "1.25rem",
          }}
        >
          <div style={cardBaseStyle}>
            <h2
              style={{
                fontSize: "1rem",
                fontWeight: 600,
                marginBottom: "0.4rem",
              }}
            >
              Actividad reciente
            </h2>
            <p
              style={{
                fontSize: "0.85rem",
                color: "#9ca3af",
              }}
            >
              Aquí podrás visualizar los últimos movimientos de clientes,
              planes y suscripciones (pendiente de conectar con la API).
            </p>
          </div>

          <div style={cardBaseStyle}>
            <h2
              style={{
                fontSize: "1rem",
                fontWeight: 600,
                marginBottom: "0.4rem",
              }}
            >
              Próximos pasos
            </h2>
            <ul
              style={{
                marginTop: "0.3rem",
                paddingLeft: "1.1rem",
                fontSize: "0.85rem",
                color: "#9ca3af",
                display: "flex",
                flexDirection: "column",
                gap: "0.2rem",
              }}
            >
              <li>Conectar tablero con API de clientes Kapos.</li>
              <li>Agregar tablas de detalle para planes y suscripciones.</li>
              <li>Incorporar métricas reales y gráficos.</li>
            </ul>
          </div>
        </section>
      </div>
    </DashboardLayout>
  );
}
