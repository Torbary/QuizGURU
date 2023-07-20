import React, { useState } from "react";

function QuestionOption({ id, value, checked, onChange }) {
  return (
    <>
      <li>
        <input
          type="radio"
          className="peer hidden"
          id={id}
          value={id}
          checked={checked}
          onChange={onChange}
        />
        <label
          htmlFor={id}
          className=" block mt-2 text-gray-900 dark:text-white font-semibold border-2 border-gray-900 dark:border-white hover:bg-sky-700 p-2 rounded-lg
        cursor-pointer peer-checked:bg-sky-800"
        >
          {value}
        </label>
      </li>
    </>
  );
}

function Question({ question, selectedOption, onOptionChange }) {
  return (
    <>
      <form className="">
        <p className="mt-4 pb-4 text-2xl mx-auto">{question.question}</p>
        {question.hint ? (
          <p className="text-lg font-sans">
            <span className="font-bold text-red-500">Hint:</span>{" "}
            {question.hint}
          </p>
        ) : null}
        <ul>
          {question.options.map((value, index) => {
            const optionId = `option_${index}`;
            return (
              <QuestionOption
                id={optionId}
                key={optionId}
                value={value}
                checked={selectedOption === optionId}
                onChange={() => onOptionChange(optionId)}
              />
            );
          })}
        </ul>
      </form>
    </>
  );
}

export default Question;
