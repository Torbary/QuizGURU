import { create } from "zustand";

export const useQuizStore = create((set) => ({
  id: "",
  index: 0,
  questions: [],
  selectedOptions: {},
  setId: (id) => set((state) => ({ ...state, id })),
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
