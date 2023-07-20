import { useQuizStore } from "../store/quiz";

function NavigationContainer() {
  const { index, setIndex, questions, selectedOptions, id } = useQuizStore();
  const length = questions.length;

  function computeAnswers() {
    const data = {};
    data.quiz_id = id;
    const answers = questions.map((value, _index) => {
      let ans = selectedOptions[_index]?.split("_")[1];
      if (ans) {
        ans = Number(ans);
      }
      return {
        question_id: value.id,
        answer: ans || -1,
      };
    });

    data.answers = answers;

    console.log(data);
  }

  function submitAnswers() {
    computeAnswers();
  }

  return (
    <div className="flex justify-between items-center mt-10">
      <div className="flex gap-1">
        <button
          className="
          bg-violet-600 hover:bg-violet-700 text-white font-bold text-base hover:rounded-sm
          transition px-3 py-2 rounded cursor-pointer disabled:bg-gray-400 disabled:cursor-not-allowed
          "
          disabled={index === 0 ? true : false}
          onClick={() => setIndex(index - 1 < 0 ? 0 : index - 1)}
        >
          Previous
        </button>
        <button
          className="
          bg-sky-500 hover:bg-sky-600 text-white font-bold text-base hover:rounded-sm
          transition px-4 py-2 rounded cursor-pointer disabled:bg-gray-400 disabled:cursor-not-allowed
          "
          disabled={index === length - 1 ? true : false}
          onClick={() => setIndex(index + 1 == length ? index : index + 1)}
        >
          Next
        </button>
      </div>
      <button
        className="transition bg-green-600 hover:bg-green-700  px-4 py-2 text-base font-bold text-white rounded
      cursor-pointer disabled:bg-gray-400 disabled:cursor-not-allowed ring-2 ring-green-300"
        onClick={submitAnswers}
      >
        Submit
      </button>
    </div>
  );
}
export default NavigationContainer;
