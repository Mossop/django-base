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

/**
 * @param {string[]} parts
 * @return {string}
 */
function path(...parts) {
  return nodePath.join(BASEDIR, ...parts);
}
exports.path = path;

/**
 * @param {object} target
 * @param {object} overrides
 * @return {void}
 */
function deep_assign_object(target, overrides) {
  for (let key of Object.keys(overrides)) {
    if (key in target && typeof target[key] === "object") {
      deep_assign_object(target[key], overrides[key]);
    } else {
      target[key] = overrides[key];
    }
  }
}

/**
 * @param {object} target
 * @param {object[]} overrides
 * @return {object}
 */
function deep_assign(target, ...overrides) {
  for (let override of overrides) {
    deep_assign_object(target, override);
  }

  return target;
}

/**
 * @param {string} file
 * @return {object}
 */
function parse(file) {
  try {
    let stats = fs.statSync(file);
    if (!stats.isFile()) {
      return {};
    }
  } catch (e) {
    return {};
  }

  return ini.parse(fs.readFileSync(file, {
    encoding: "utf8",
  }));
}

let config = deep_assign(
  parse(path("base", "defaults.ini")),
  parse(path("config", "config.ini")),
  parse(path("config.ini")),
);

exports.config = config;
