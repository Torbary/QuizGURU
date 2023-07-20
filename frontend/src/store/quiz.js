import { create } from "zustand";

export const useQuizStore = create((set) => ({
  index: 0,
  questions: [],
  selectedOptions: {},
  setIndex: (index) => set((state) => ({ ...state, index })),
  setQuestions: (newQuestions) =>
    set((state) => ({ ...state, questions: newQuestions })),
  setSelectedOptions: (questionIndex, optionId) =>
    set((state) => ({
      selectedOptions: {
        ...state.selectedOptions,
        [questionIndex]: optionId,
      },
    })),
}));
