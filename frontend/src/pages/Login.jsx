import React from "react";
import DivInput from "../components/div-input";

export default function Login() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <form
        className="max-w-[420px] min-w-[380px] mx-auto px-8 py-9 rounded-lg
       bg-[rgba(235,95,95,0.13)] backdrop-blur-md"
      >
        <h1 className="text-center text-3xl mb-4">Login In Your Account</h1>

        <DivInput
          type="email"
          name="email"
          id="email-input"
          label="Email"
          placeholder="e.g janedoe@domain.com"
        />
        <DivInput
          type="password"
          name="password"
          id="password-input"
          label="Password"
          placeholder="Jane123@"
        />
        <button
          className="w-full h-12 transition ease-in hover:bg-sky-900 bg-sky-700
         text-white mt-8 font-semibold text-xl"
        >
          Log In
        </button>
        <p className="mt-4 text-center text-base mx-auto">
          Don't have an account?{" "}
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
