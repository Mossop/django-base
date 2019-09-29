/* eslint-env node */

const nodePath = require("path");
const fs = require("fs");

const ini = require("ini");

const BASE = nodePath.resolve(__dirname);
exports.BASE = BASE;
const BASEDIR = nodePath.dirname(BASE);
exports.BASEDIR = BASEDIR;
const PROJECT = nodePath.basename(BASEDIR);
exports.PROJECT = PROJECT;

function path(...parts) {
  return nodePath.join(BASEDIR, ...parts);
}
exports.path = path;

function assign(source, overrides) {
  if (typeof source === "object" && typeof overrides === "object") {
    for (let key of Object.keys(overrides)) {
      if (key in source) {
        source[key] = assign(source[key], overrides[key]);
      } else {
        source[key] = overrides[key];
      }
    }

    return source;
  } else {
    return overrides;
  }
}

function parse(config, ...parts) {
  let file = path(...parts);
  try {
    let stats = fs.statSync(file);
    if (!stats.isFile()) {
      return;
    }
  } catch (e) {
    return;
  }

  return assign(config, ini.parse(fs.readFileSync(file, {
    encoding: "utf8",
  })));
}

let config = parse(undefined, "base", "defaults.ini");
config = parse(config, "config", "config.ini");
config = parse(config, "config.ini");

exports.config = config;
