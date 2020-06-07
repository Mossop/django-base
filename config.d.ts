/* eslint @typescript-eslint/no-explicit-any: "off" */
export const BASE: string;
export const BASEDIR: string;
export const PROJECT: string;

export function path(...parts: string[]): string;

interface GeneralConfig {
  debug: boolean;
}

export interface Config {
  path: Record<string, string>;
  url: Record<string, string>;
  general?: GeneralConfig;
}

export const config: Config;
