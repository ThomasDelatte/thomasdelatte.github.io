Title: GPT2-generated EU legislation
Slug: gpt2

<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
</head>
<body>
	<section id="main" class="section">
		<div class="container">
			<div class="columns is-variable is-5">
				<div class="column is-narrow" style="width: 250px;">
					<form id="gen-form">
						<div class="field">
							<label class="label">Text Prompt</label>
							<div class="control">
								<textarea id="prefix" class="textarea" type="text" placeholder="Council Directive" rows="2"></textarea>
							</div>
							<p class="help">Starts the generated text with the specified text. <em>(Optional: max 500 characters)</em>
							</p>
						</div>
						<div class="field">
							<label class="label">Generated Text Length</label>
							<div class="control">
								<input id="length" class="input" type="text" placeholder="Text input" value="500">
							</div>
							<p class="help">Length of the text in tokens to generate. <em>(max: 1023)</em></p>
						</div>
						<div class="field">
							<label class="label">Temperature</label>
							<div class="control">
								<input id="temperature" class="input" type="text" placeholder="0.8" value="0.8">
							</div>
							<p class="help">Controls the generated text "creativity." <em>(the higher the temperature, the more	creative)</em></p>
						</div>
						<div class="field">
							<label class="label">Top <em>k</em></label>
							<div class="control">
								<input id="top_k" class="input" type="text" placeholder="40" value="40">
							</div>
							<p class="help">Constrains the generated text tokens to the top <em>k</em> possibilities. <em>(set to 0 to
									disable)</em></p>
						</div>
						<div class="buttons">
							<span class="control">
								<button type="submit" name="submit" id="generate-text" class="button is-link">
									<span class="icon">
										<i class="fas fa-md fa-pen"></i>
									</span><span>Generate Text!</span></button>
							</span>
						</div>
					</form>
					<div id="extra-buttons" class="buttons">
						<span class="control">
							<button id="save-image" class="button is-success">
								<span class="icon">
									<i class="fas fa-md fa-save"></i>
								</span><span>Save Image</span></button>
						</span>
						<span class="control">
							<button id="clear-text" class="button is-danger">
								<span class="icon">
									<i class="fas fa-md fa-trash-alt"></i>
								</span><span>Clear Texts</span< /button> </span> </div>
				</div>
				<div id="model-output" class="column">
					<p id="tutorial" text-align="right" class="subtitle"><em>Generated text will appear here!
							Use the form to configure GPT-2 and press <strong>Generate Text</strong>
							to get your own text!
						</em></p>
				</div>
			</div>
		</div>
	</section>
</body>

<script src="https://code.jquery.com/jquery-3.4.1.min.js"
	integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous">
	</script>

<script src="http://html2canvas.hertzen.com/dist/html2canvas.min.js">
</script>

<script type="text/javascript">
	$(function () {
		$('#gen-form').submit(function (e) {
			e.preventDefault();
			$.ajax({
				type: "POST",
				url: "https://eu-text-generator-lpl4nmyypq-ew.a.run.app",
				dataType: "json",
				data: JSON.stringify(getInputValues()),
				beforeSend: function (data) {
					$('#generate-text').addClass("is-loading");
					$('#generate-text').prop("disabled", true);
				},
				success: function (data) {
					$('#generate-text').removeClass("is-loading");
					$('#generate-text').prop("disabled", false);
					$('#tutorial').remove();
					var gentext = data.text;
					if ($("#prefix").length & $("#prefix").val() != '') {
						var pattern = new RegExp('^' + $("#prefix").val(), 'g');
						var gentext = gentext.replace(pattern, '<strong>' + $("#prefix").val() + '</strong>');
					}

					var gentext = gentext.replace(/\n\n/g, "<div><br></div>").replace(/\n/g, "<div></div>");
					var html = '<div class=\"gen-box\">' + gentext + '</div><div class="gen-border"></div>';
					$(html).appendTo('#model-output').hide().fadeIn("slow");
				},
				error: function (jqXHR, textStatus, errorThrown) {
					$('#generate-text').removeClass("is-loading");
					$('#generate-text').prop("disabled", false);
					$('#tutorial').remove();
					var html = '<div class="gen-box warning">There was an error generating the text! Please try again!</div><div class="gen-border"></div>';
					$(html).appendTo('#model-output').hide().fadeIn("slow");
				}
			});
		});
		$('#clear-text').click(function (e) {
			$('#model-output').text('')
		});

		// https://stackoverflow.com/a/51478809
		$("#save-image").click(function () {

			html2canvas(document.querySelector('#model-output')).then(function (canvas) {

				saveAs(canvas.toDataURL(), 'gen_texts.png');
			});
		});

	});

	function getInputValues() {
		var inputs = {};
		$("textarea, input").each(function () {
			inputs[$(this).attr('id')] = $(this).val();
		});
		return inputs;
	}

	// https://stackoverflow.com/a/51478809
	function saveAs(uri, filename) {

		var link = document.createElement('a');

		if (typeof link.download === 'string') {

			link.href = uri;
			link.download = filename;

			//Firefox requires the link to be in the body
			document.body.appendChild(link);

			//simulate click
			link.click();

			//remove the link when done
			document.body.removeChild(link);

		} else {

			window.open(uri);

		}
	}
</script>
</html>

<style>
	html,
	body {
		height: 95% !important;
		margin: 0 !important;
	}

	footer {
		/*max-height: 5% !important;*/
		padding: 1em !important
	}

	section {
		min-height: 95% !important
	}

	.gen-box {
		background-color: #fff;
		display: block;
		padding: 1.25rem;
		color: #4a4a4a;
		font-size: 1rem;
		font-weight: 400;
		line-height: 1.25;
    }

	.gen-border {
		height: 0.25em;
		background-color: #d5d5d5;
	}

	.gen-box.warning {
		color: red;
		font-weight: 700;

	}

	.brand-text {
		display: flex;
		align-items: center;
		font-size: 1.5em
	}

	#extra-buttons {
		padding-top: 1em;
		margin-top: 1em;
		border-top: 0.5px solid #d5d5d5;
	}
</style>