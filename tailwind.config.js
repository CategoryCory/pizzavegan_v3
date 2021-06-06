const colors = require("tailwindcss/colors");

module.exports = {
  purge: [
      "{articles,dashboard,home,pages,pizzavegan,pizzerias,products,recipes,search,templates}/**/{*.html,forms.py}",
      // "contacts/forms.py",
      // "users/forms.py",
      // "dashboard/forms.py",
      "pizzeria_map_svjs/src/**/*.{js,svelte}"
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      "sans": ["Jost", "ui-sans-serif", "system-ui", "-apple-system", "BlinkMacSystemFont", '"Segoe UI"', "Roboto", '"Helvetica Neue"', "Arial", '"Noto Sans"', "sans-serif", '"Apple Color Emoji"', '"Segoe UI Emoji"', '"Segoe UI Symbol"', '"Noto Color Emoji"'],
      "serif": ["Lora", "ui-serif", "Georgia", "Cambria", '"Times New Roman"', "Times", "serif"]
    },
    extend: {
      colors: {
        brand: {
          DEFAULT: "#B45A7E",
          light: "#CE7498",
          dark: "#9B4165",
          extradark: "#680E32"
        },
        secondary: {
          DEFAULT: "#3fa649",
          light: "#53BA5D",
          dark: "#2B9235"
        },
        gray: colors.warmGray,
        coolgray: colors.coolGray
      },
      typography: {
        brand: {
          css: {
            a: {
              color: "#B45A7E",
              "&:hover": {
                color: "#9B4165"
              }
            }
          }
        }
      }
    },
  },
  variants: {
    extend: {
      opacity: ['disabled'],
    },
  },
  plugins: [
      require("@tailwindcss/typography"),
      require("@tailwindcss/forms")
  ],
}
