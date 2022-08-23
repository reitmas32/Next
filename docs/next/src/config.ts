export const SITE = {
	title: 'Next',
	description: 'Manage your Next app development.',
	defaultLanguage: 'en_US',
};

export const OPEN_GRAPH = {
	image: {
		src: 'https://github.com/withastro/astro/blob/main/assets/social/banner.jpg?raw=true',
		alt:
			'astro logo on a starry expanse of space,' +
			' with a purple saturn-like planet floating in the right foreground',
	},
	twitter: 'astrodotbuild',
};

export const KNOWN_LANGUAGES = {
	English: 'en',
};

// Uncomment this to add an "Edit this page" button to every page of documentation.
// export const GITHUB_EDIT_URL = `https://github.com/withastro/astro/blob/main/docs/`;

// Uncomment this to add an "Join our Community" button to every page of documentation.
// export const COMMUNITY_INVITE_URL = `https://astro.build/chat`;

// Uncomment this to enable site search.
// See "Algolia" section of the README for more information.
// export const ALGOLIA = {
//   indexName: 'XXXXXXXXXX',
//   appId: 'XXXXXXXXXX',
//   apiKey: 'XXXXXXXXXX',
// }

export const SIDEBAR = {
	en: [
		{ text: '', header: true },
		{ text: 'Get Started', header: true },
		{ text: 'Introduction', link: 'en/get_started/introduction' },
		{ text: 'Install and Setup', link: 'en/get_started/install' },
		{ text: 'First Project', link: 'en/get_started/first_project' },
		{ text: 'Config.yaml Basic', link: 'en/get_started/config_yaml_basic' },

		{ text: 'Examples', header: true },
		{ text: 'Empty Project', link: 'en/examples/empty_project' },
		{ text: 'Basic_Library', link: 'en/examples/basic_library' },
		{ text: 'Project With Dependencies', link: 'en/examples/project_with_dependencies' },

		{ text: 'Builders', header: true },
		{ text: 'Cmake', link: 'en/builders/cmake' },
		{ text: 'Basic', link: 'en/builders/basic' },

		{ text: 'Commands', header: true },
		{ text: 'Create', link: 'en/commands/create' },
		{ text: 'Build', link: 'en/commands/build' },
		{ text: 'Clean', link: 'en/commands/clean' },
		{ text: 'Info', link: 'en/commands/info' },
		{ text: 'Version', link: 'en/commands/version' },
		{ text: 'Tree', link: 'en/commands/tree' },
		{ text: 'Run', link: 'en/commands/run' },
		{ text: 'Export', link: 'en/commands/export' },
		{ text: 'Import', link: 'en/commands/import' },
		{ text: 'Get', link: 'en/commands/get' },
		{ text: 'Set', link: 'en/commands/set' },
		{ text: 'Add', link: 'en/commands/add' },
		{ text: 'Exce', link: 'en/commands/exce' },
		{ text: 'Check_env', link: 'en/commands/check_env' },
	],
};
