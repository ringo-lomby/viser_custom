from __future__ import annotations

HUD_HTML = """
<style>
	.unified-hud {
		position: fixed;
		top: 20px;
		left: 50%;
		transform: translateX(-50%);
		width: 90%; /* Increased width */
		max-width: 1200px; /* Increased max-width */
		background-color: rgba(255, 255, 255, 0.03);
		border-radius: 10px;
		color: #FFFFFF;
		font-family: 'Chakra Petch', sans-serif;
		font-weight: bold;
		z-index: 999990;
		display: flex;
		justify-content: space-around;
		align-items: center;
		padding: 15px; /* Increased padding */
		backdrop-filter: blur(10px); /* Increased blur for stronger glass effect */
		border: 1px solid rgba(255, 255, 255, 0.4); /* Subtle white border for reflection */
		transition: opacity 0.2s ease-in-out; /* Added for smoother transitions */
	}
</style>
"""
