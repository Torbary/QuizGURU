import { Link, useNavigate } from "react-router-dom";

export default function ErrorPage() {
  return (
    <div className="min-h-screen flex gap-2 flex-col justify-center items-center">
      <h1 className="text-4xl">Oops!</h1>
      <p className="text-2xl">Sorry, an unexpected error has occurred.</p>
      <Link
        to={"/"}
        className="border text-xl p-2 m-2 rounded-lg hover:bg-gray-300 hover:text-blue-900 transition-all"
      >
        Go Home
      </Link>
    </div>
  );
}
