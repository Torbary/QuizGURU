/* eslint-disable react/prop-types */
import { useQuizStore } from "../store/quiz";

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
          className="block mt-2 text-gray-900 dark:text-white font-semibold
          border-2 border-gray-900 dark:border-white hover:bg-sky-700 p-2
          rounded-lg cursor-pointer peer-checked:bg-sky-800
          "
        >
          {value}
        </label>
      </li>
    </>
  );
}

function Question() {
  const { questions, index, selectedOptions, setSelectedOptions } =
    useQuizStore();
  const onOptionChange = (optionId) => {
    setSelectedOptions(index, optionId);
  };
  const question = questions[index];
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
          {question.options.map((value, _index) => {
            const optionId = `option_${_index}`;
            return (
              <QuestionOption
                id={optionId}
                key={optionId}
                value={value}
                checked={selectedOptions[index] === optionId}
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
