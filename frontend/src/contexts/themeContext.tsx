import { useState, useEffect, useContext, useRef } from "react";
import { createContext } from "react";
import { SSEContext } from "./webSocketContext";
export const ThemeContext = createContext<any>(undefined);
export function ThemeProvider({ children }: any) {
  const wsContext: any = useContext(SSEContext);
  const [theme, setTheme] = useState(null);
  const themeRef = useRef(theme);
  useEffect(() => {
    const newTheme = wsContext?.data?.settings?.theme;
    if (themeRef.current !== newTheme?.value) {
      setTheme(newTheme?.value);
      themeRef.current = newTheme?.value;
    }
  }, [wsContext]);

  return (
    <ThemeContext.Provider value={theme}>{children}</ThemeContext.Provider>
  );
}
