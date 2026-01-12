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
	.hud-item {
		display: flex;
        flex-direction: column;
        align-items: center;
	}
	.speed-gauge {
		position: relative;
		width: 150px;
		height: 150px;
	}
	.speed-value {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		font-size: 96px;
	}
	.speed-unit {
		font-size: 24px;
	}
	.battery-bar-container {
		width: 150px;
		height: 20px;
		background-color: #333;
		border-radius: 5px;
		overflow: hidden;
	}
	.battery-bar-fill {
		height: 100%;
		border-radius: 5px;
	}
	.battery-value {
		font-size: 48px;
	}
	.battery-label {
		font-size: 36px;
	}
	.mission-info {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.mission-label {
		font-size: 24px;
		margin-bottom: 5px;
	}
	.mission-data {
		font-size: 48px;
	}
	.mission-unit {
		font-size: 24px; /* Smaller font size for units */
	}
	.traffic-light {
		width: 100px;
		height: 100px;
		border-radius: 50%;
		background-color: #808080;
		border: 2px solid #FFFFFF;
	}
</style>
"""
