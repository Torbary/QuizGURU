import React from "react";
import DivInput from "../components/div-input";
import { useNavigate } from "react-router";

const initialForm = {
  email: "",
  password: "",
};

export default function Login() {
  const [form, setForm] = React.useState(initialForm);
  const [error, setError] = React.useState("");
  const [isLoading, setIsLoading] = React.useState(false);
  const navigate = useNavigate();

  const handleChange = (event) => {
    event.preventDefault();
    setForm({
      ...form,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const headers = {
      Accept: "*/*",
      "User-Agent": "Thunder Client (https://www.thunderclient.com)",
      "Content-Type": "application/json",
    };

    try {
      setIsLoading(true);
      let response = await fetch(`${import.meta.env.VITE_API_URL}/login`, {
        method: "POST",
        body: JSON.stringify(form),
        headers: headers,
      });

      if (response.ok) {
        navigate("/");
        console.log(await response.json());
      } else {
        const text = await response.text();
        console.log(text);
        setError(text);
      }

      setIsLoading(false);
    } catch (err) {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <form
        onSubmit={handleSubmit}
        className="max-w-[420px] min-w-[380px] mx-auto px-8 py-9 rounded-lg
       bg-[rgba(235,95,95,0.13)] backdrop-blur-md"
      >
        <h1 className="text-center text-3xl mb-4">Login In Your Account</h1>
        {error.length !== 0 ? (
          <div className="px-2 py-2 text-center bg-red-600 mb-4 text-slate-950 text-lg font-semibold">
            {error}
          </div>
        ) : (
          ""
        )}

        <DivInput
          type="email"
          name="email"
          id="email-input"
          label="Email"
          placeholder="e.g janedoe@domain.com"
          value={form.email}
          onChange={handleChange}
        />
        <DivInput
          type="password"
          name="password"
          id="password-input"
          label="Password"
          placeholder="Jane123@"
          value={form.password}
          onChange={handleChange}
        />
        <button
          className="w-full h-12 transition ease-in hover:bg-sky-900 bg-sky-700
         text-white mt-8 font-semibold text-xl disabled:bg-gray-400 disabled:cursor-not-allowed"
          disabled={isLoading === true}
        >
          {isLoading !== true ? "Log In" : "Loading..."}
        </button>
        <p className="mt-4 text-center text-base mx-auto">
          Don&apos;t have an account ?{" "}
          <a
            href="/register"
            className="text-lg text-blue-500 dark:text-amber-300 hover:text-emerald-800"
          >
            sign-up
          </a>{" "}
          instead.
        </p>
      </form>
    </div>
  );
}
