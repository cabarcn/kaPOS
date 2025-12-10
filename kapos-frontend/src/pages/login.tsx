// src/pages/login.tsx
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api/auth";

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState("admin_api");
  const [password, setPassword] = useState("pass123");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [userInfo, setUserInfo] = useState<any>(null);

  const navigate = useNavigate();

  // Si ya hay token y alguien entra a /login, lo mandamos directo al dashboard
  useEffect(() => {
    const token = localStorage.getItem("kapos_access");
    if (token) {
      navigate("/dashboard", { replace: true });
    }
  }, [navigate]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const data = await login(username, password);

      // Guardar tokens y usuario en localStorage
      if (data.access) {
        localStorage.setItem("kapos_access", data.access);
      }
      if (data.refresh) {
        localStorage.setItem("kapos_refresh", data.refresh);
      }
      if (data.user) {
        localStorage.setItem("kapos_user", JSON.stringify(data.user));
        setUserInfo(data.user);
      }

      // Redirigir al dashboard
      navigate("/dashboard");
    } catch (err: any) {
      console.error(err);
      setUserInfo(null);
      setError(err.message || "Error inesperado al iniciar sesión");
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("kapos_access");
    localStorage.removeItem("kapos_refresh");
    localStorage.removeItem("kapos_user");
    setUserInfo(null);
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "#020617",
        padding: "1rem",
      }}
    >
      <div
        style={{
          background: "#020617",
          borderRadius: "18px",
          padding: "2.2rem 2.4rem",
          maxWidth: "420px",
          width: "100%",
          boxShadow: "0 20px 40px rgba(0,0,0,0.5)",
          border: "1px solid rgba(148, 163, 184, 0.35)",
          color: "#e5e7eb",
        }}
      >
        <h1
          style={{
            fontSize: "1.8rem",
            marginBottom: "0.25rem",
            fontWeight: 700,
          }}
        >
          KApos Panel
        </h1>
        <p style={{ marginBottom: "1.5rem", color: "#9ca3af" }}>
          Inicia sesión para administrar clientes, planes y suscripciones.
        </p>

        {/* Mensaje si ya hay sesión iniciada */}
        {userInfo && (
          <div
            style={{
              marginBottom: "1.5rem",
              padding: "0.75rem 1rem",
              borderRadius: "12px",
              background:
                "linear-gradient(90deg, rgba(34,197,94,0.15), rgba(34,197,94,0.05))",
              border: "1px solid rgba(34,197,94,0.4)",
              fontSize: "0.9rem",
            }}
          >
            Sesión iniciada como{" "}
            <strong>{userInfo.username ?? "admin_api"}</strong>{" "}
            <span
              style={{
                textTransform: "capitalize",
                opacity: 0.9,
              }}
            >
              ({userInfo.rol ?? "Admin"})
            </span>
          </div>
        )}

        <form
          onSubmit={handleSubmit}
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "1rem",
          }}
        >
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              gap: "0.35rem",
            }}
          >
            <label style={{ fontSize: "0.9rem" }}>Usuario</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              style={{
                padding: "0.55rem 0.75rem",
                borderRadius: "9999px",
                border: "1px solid #4b5563",
                background: "#020617",
                color: "#e5e7eb",
                outline: "none",
              }}
              placeholder="Ej: admin_api"
            />
          </div>

          <div
            style={{
              display: "flex",
              flexDirection: "column",
              gap: "0.35rem",
            }}
          >
            <label style={{ fontSize: "0.9rem" }}>Contraseña</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{
                padding: "0.55rem 0.75rem",
                borderRadius: "9999px",
                border: "1px solid #4b5563",
                background: "#020617",
                color: "#e5e7eb",
                outline: "none",
              }}
              placeholder="********"
            />
          </div>

          {error && (
            <div
              style={{
                fontSize: "0.85rem",
                color: "#fca5a5",
                background: "rgba(248,113,113,0.1)",
                borderRadius: "8px",
                padding: "0.5rem 0.75rem",
              }}
            >
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            style={{
              marginTop: "0.5rem",
              padding: "0.6rem 0.75rem",
              borderRadius: "9999px",
              border: "none",
              cursor: loading ? "wait" : "pointer",
              background: loading
                ? "rgba(59,130,246,0.4)"
                : "linear-gradient(90deg, #3b82f6, #22c55e)",
              color: "#0b1120",
              fontWeight: 600,
              fontSize: "0.95rem",
            }}
          >
            {loading ? "Ingresando..." : "Iniciar sesión"}
          </button>
        </form>

        {userInfo && (
          <div
            style={{
              marginTop: "1.5rem",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              fontSize: "0.85rem",
            }}
          >
            <span style={{ color: "#9ca3af" }}>
              Token guardado en el navegador (localStorage).
            </span>
            <button
              type="button"
              onClick={handleLogout}
              style={{
                border: "none",
                background: "transparent",
                color: "#f97316",
                cursor: "pointer",
                textDecoration: "underline",
              }}
            >
              Cerrar sesión
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default LoginPage;
