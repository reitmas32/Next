import type { FunctionalComponent } from 'preact';
import { h, Fragment } from 'preact';
import { useState, useEffect } from 'preact/hooks';

const GitHubButton: FunctionalComponent = () => {
	const [sidebarShown, setSidebarShown] = useState(false);

	useEffect(() => {
		const body = document.getElementsByTagName('body')[0];
		if (sidebarShown) {
			body.classList.add('mobile-sidebar-toggle');
		} else {
			body.classList.remove('mobile-sidebar-toggle');
		}
	}, [sidebarShown]);
	
	return (
		<button>
			<img src="../../public/github.svg" alt="my image" onClick={(e) => {
			e.preventDefault();
			window.location.href='https://github.com/reitmas32/Next';
			}} />
		</button>
	);
};

export default GitHubButton;