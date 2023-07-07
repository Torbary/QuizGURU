import React from "react";
function NavigationContainer({ length, index, setIndex }) {

    const handleNext = () => {
        setIndex((currentIndex) => {
            return currentIndex + 1 == length ? currentIndex : currentIndex + 1
        })
    }
    const handlePrevious = () => {
        setIndex((currentIndex) => {
            return currentIndex - 1 < 0 ? 0 : currentIndex - 1
        })
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
          onClick={handlePrevious}
        >
          Previous
        </button>
        <button
          className="
          bg-sky-500 hover:bg-sky-600 text-white font-bold text-base hover:rounded-sm
          transition px-4 py-2 rounded cursor-pointer disabled:bg-gray-400 disabled:cursor-not-allowed
          "
          disabled={index === length - 1 ? true : false}
          onClick={handleNext}
        >
          Next
        </button>
      </div>
      <button
        className="transition bg-green-600 hover:bg-green-700  px-4 py-2 text-base font-bold text-white rounded
      cursor-pointer disabled:bg-gray-400 disabled:cursor-not-allowed ring-2 ring-green-300"
      >
        Submit
      </button>
    </div>
  );
}
export default NavigationContainer;
