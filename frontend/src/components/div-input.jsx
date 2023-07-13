import React from "react";

export default function DivInput(props) {
  return (
    <div className="mb-4">
      <label htmlFor={props?.id} className="font-semibold text-lg">
        {props.label}
      </label>
      <input
        type={props.type || "text"}
        className={
          props?.className ||
          "block transition-all w-full h-10 px-2 mt-2 text-base text-white font-semibold rounded-sm outline-1 outline-gray-600 bg-zinc-800 dark:bg-slate-700"
        }
        name={props?.name}
        id={props?.id}
        onChange={props?.onChange}
        placeholder={props?.placeholder}
      ></input>
    </div>
  );
}
