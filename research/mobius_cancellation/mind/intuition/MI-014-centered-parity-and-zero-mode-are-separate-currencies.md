# MI-014 — The rough zero mode can be reached nonlinearly only by paying a source-correlation bill

**Evidence level:** exact sector protection and nonlinear source expansions through MC-196

## Core intuition

The rough principal Möbius mean is protected from the canonical transverse coordinate systems tested so far, but nonlinear operations reveal a more precise boundary. Pointwise nonlinearities can formally mix frequencies back into the principal sector without creating new arithmetic information; genuinely aggregated nonlinearities can create principal/transverse coupling, but then expose explicit higher source correlations that must be controlled at the growing arithmetic scale.

Thus “nonlinear” is not itself the missing category. The useful question is whether a nonlinear relation reaches the principal mode **with a cheaper source obligation than the fixed-power cancellation one is trying to prove**.

## Strongest justified principle

MC-185--MC-194 separate centered fluctuations from the rough zero mode and show that characters, CRT transport, additive shells, and the full additive image of a residue vector preserve the relevant sector decomposition. The principal obligation survives those coordinate changes.

MC-195 then uses `mu^3=mu`. Although the associated cubic transverse triad algebraically returns to frequency zero, the canonical cubic statistic reduces exactly to `m_N(1-3s_N+2m_N^2)` and is therefore Mertens-complete: its smallness is equivalent in scale to the original principal mean. More generally, every one-site function of ternary Möbius data is only quadratic in `1,mu,mu^2`.

MC-196 aggregates before cubing and obtains a genuinely new principal-mode interaction. The exact expansion, however, introduces ordered same-residue pair and triple correlations. At primorial modulus `q=X^{c+o(1)}` these are polynomial-shift correlation sums; generic high-moment or almost-all Chowla information incurs a polynomial `q`-dependent restriction cost and does not automatically deliver the fixed power.

## Program consequence

Admit nonlinear routes only after writing their exact source expansion. Prefer identities in which the dangerous pair/triple terms cancel by algebra, factorization, or cross-scale conservation. Otherwise the task is to prove the required same-residue correlations uniformly in the growing modulus, and that cost must be compared directly with the desired principal estimate.

## Counterevidence / boundary

MC-196 does not prove that all nonlinear principal couplings are Mertens-complete or source-expensive. A different inter-site identity, a multiscale relation, or a factorization law could cancel the correlation bill. The current no-go applies to the tested pointwise and primorial-cubic mechanisms.

## Epistemic status

**Exact protection of the principal mode under canonical linear coordinates, exact closure of pointwise cubic mixing, and a concrete nonlinear escape whose price is polynomial-shift source correlation; a cheaper source-forced coupling remains open.**

## Falsification criterion

Exhibit a covered canonical linear operation that transfers transverse cancellation into the principal mean, or a nonlinear operation whose exact principal-mode expansion avoids both Mertens-equivalent terms and uncontrolled growing-modulus source correlations while remaining source-forced.