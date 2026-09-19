// Global JSX namespace for React element rendering
declare namespace JSX {
  interface Element {
    [key: string]: any;
  }
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}

// Global React namespace for ambient type usage (e.g. React.FC, React.ElementType)
declare namespace React {
  type ReactNode = any;
  type ReactElement<P = any, T = any> = any;
  type Component<P = {}, S = {}> = any;
  type ComponentType<P = any> = any;
  type ElementType<P = any> = any;
  type FC<P = {}> = (props: P) => any;
  type FunctionComponent<P = {}> = FC<P>;
  type MouseEvent<T = any> = any;
  type FormEvent<T = any> = any;
  type ChangeEvent<T = any> = any;
  type CSSProperties = any;
  type Ref<T = any> = any;
  interface RefObject<T> {
    readonly current: T | null;
  }
  interface MutableRefObject<T> {
    current: T;
  }

  function useState<T>(initialState: T | (() => T)): [T, (newState: T | ((prevState: T) => T)) => void];
  function useState<T = any>(initialState?: any): [T, (newState: any) => void];
  function useEffect(effect: () => void | (() => void), deps?: readonly any[]): void;
  function useLayoutEffect(effect: () => void | (() => void), deps?: readonly any[]): void;
  function useCallback<T extends (...args: any[]) => any>(callback: T, deps: readonly any[]): T;
  function useMemo<T>(factory: () => T, deps: readonly any[] | undefined): T;
  function useRef<T>(initialValue: T): MutableRefObject<T>;
  function useRef<T>(initialValue: T | null): RefObject<T>;
  function useRef<T = any>(initialValue?: any): MutableRefObject<T>;
  function useContext<T = any>(context: any): T;
  function useReducer<R extends (...args: any[]) => any>(reducer: R, initialState: any, init?: any): any;
  function createContext<T = any>(defaultValue?: T): any;
  function forwardRef<T = any, P = {}>(render: (props: P, ref: any) => any): any;
  function memo<T = any>(Component: T): T;
  const Fragment: any;
  const Suspense: any;
}

// Ambient module for 'react'
declare module "react" {
  export type ReactNode = any;
  export type ReactElement<P = any, T = any> = any;
  export type ComponentType<P = any> = any;
  export type ElementType<P = any> = any;
  export type FC<P = {}> = (props: P) => any;
  export type FunctionComponent<P = {}> = FC<P>;
  export type MouseEvent<T = any> = any;
  export type FormEvent<T = any> = any;
  export type ChangeEvent<T = any> = any;
  export type CSSProperties = any;
  export interface RefObject<T> {
    readonly current: T | null;
  }
  export interface MutableRefObject<T> {
    current: T;
  }
  export type Ref<T = any> = any;

  export function useState<T>(initialState: T | (() => T)): [T, (newState: T | ((prevState: T) => T)) => void];
  export function useState<T = any>(initialState?: any): [T, (newState: any) => void];
  export function useEffect(effect: () => void | (() => void), deps?: readonly any[]): void;
  export function useLayoutEffect(effect: () => void | (() => void), deps?: readonly any[]): void;
  export function useCallback<T extends (...args: any[]) => any>(callback: T, deps: readonly any[]): T;
  export function useMemo<T>(factory: () => T, deps: readonly any[] | undefined): T;
  export function useRef<T>(initialValue: T): MutableRefObject<T>;
  export function useRef<T>(initialValue: T | null): RefObject<T>;
  export function useRef<T = any>(initialValue?: any): MutableRefObject<T>;
  export function useContext<T = any>(context: any): T;
  export function useReducer<R extends (...args: any[]) => any>(reducer: R, initialState: any, init?: any): any;
  export function createContext<T = any>(defaultValue?: T): any;
  export function forwardRef<T = any, P = {}>(render: (props: P, ref: any) => any): any;
  export function memo<T = any>(Component: T): T;
  export const Fragment: any;
  export const Suspense: any;

  export namespace JSX {
    interface Element {
      [key: string]: any;
    }
    interface IntrinsicElements {
      [elemName: string]: any;
    }
  }

  const React: any;
  export default React;
}

// Ambient module for React 17+ JSX runtimes
declare module "react/jsx-runtime" {
  export const jsx: any;
  export const jsxs: any;
  export const Fragment: any;
  export namespace JSX {
    interface Element {
      [key: string]: any;
    }
    interface IntrinsicElements {
      [elemName: string]: any;
    }
  }
}

declare module "react/jsx-dev-runtime" {
  export const jsxDEV: any;
  export const Fragment: any;
  export namespace JSX {
    interface Element {
      [key: string]: any;
    }
    interface IntrinsicElements {
      [elemName: string]: any;
    }
  }
}

// Ambient module for 'framer-motion'
declare module "framer-motion" {
  export const motion: any;
  export const AnimatePresence: any;
  const framerMotion: any;
  export default framerMotion;
}

// Ambient module for 'lucide-react'
declare module "lucide-react" {
  export const ArrowUpRight: any;
  export const Bot: any;
  export const Sparkles: any;
  export const MessageSquare: any;
  export const BookOpen: any;
  export const PenTool: any;
  export const BookMarked: any;
  export const Mic: any;
  export const Trophy: any;
  export const ShieldCheck: any;
  export const Server: any;
  export const Zap: any;
  export const Copy: any;
  export const Check: any;
  export const CheckCircle2: any;
  export const Cpu: any;
  export const Database: any;
  export const AlertCircle: any;
  export const Clock: any;
  export const Layers: any;
  export const Activity: any;
  export const ExternalLink: any;
  export const Info: any;
  export const Terminal: any;
  export const RefreshCw: any;
  export const Play: any;
  const icons: any;
  export default icons;
}

