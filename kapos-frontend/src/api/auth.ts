// src/api/auth.ts

export interface UserInfo {
  id: number;
  username: string;
  email: string;
  rol: string;
}

export interface LoginResponse {
  access: string;
  refresh: string;
  user: UserInfo;
}

export async function login(
  username: string,
  password: string
): Promise<LoginResponse> {
  const response = await fetch("http://localhost:8000/api/usuarios/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  });

  if (!response.ok) {
    throw new Error("Credenciales incorrectas");
  }

  const data = (await response.json()) as LoginResponse;

  // 👀 Para ver exactamente qué está mandando el backend
  console.log("Respuesta login backend:", data);

  // Guarda tokens e info de usuario
  localStorage.setItem("kapos_access", data.access);
  localStorage.setItem("kapos_refresh", data.refresh);
  localStorage.setItem("kapos_user", JSON.stringify(data.user));

  return data;
}
