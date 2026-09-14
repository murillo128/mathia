# PL-303 — The certified odd spectral gap does not smooth the localized-Weil resolvent into BV

**Evidence:** `LITERATURE+EXACT-DERIVED + DECISIVE-REGULARITY-OBSTRUCTION`

**Status:** `GAP-ONLY-BV-ROUTE-CLOSED + SOURCE-SPECIFIC-COMMUTATOR-ESTIMATE-REQUIRED`

## Claim

The live uniform-BV route left by `PL-299`--`PL-302` cannot be closed merely by combining the simple even ground state at aperture `a=0.8` with the certified odd-sector spectral gap from `PL-284`. The exact localized-Weil operator itself has too little high-frequency coercivity for its odd resolvent to smooth arbitrary `L^2` data into bounded variation.

Let `I=(-1,1)` and let `\widetilde A_{0.8}` be Suzuki's fixed-domain realization of the canonical localized completed-Weil operator, unitarily equivalent under the standard spatial rescaling to `A_{0.8}`. Reflection reduces the operator into even and odd sectors. Let `lambda_1` be its simple even ground level, and write `\widetilde A^-_{0.8}` for the odd restriction. The certified bounds transferred in `PL-284` give

\[
\lambda_1\le 2.27\times10^{-17},
\qquad
\inf\sigma(\widetilde A^-_{0.8})\ge 8.206\times10^{-15},
\]

so

\[
d:=\operatorname{dist}(\lambda_1,\sigma(\widetilde A^-_{0.8}))
\ge 8.1833\times10^{-15}>0.
\]

Hence the odd resolvent

\[
R^-=(\widetilde A^-_{0.8}-\lambda_1)^{-1}
\]

is perfectly bounded on `L^2_odd(I)`, with `||R^-||_{2->2}<=d^{-1}`. Nevertheless

\[
\boxed{
R^-:L^2_{\rm odd}(I)\not\longrightarrow BV_0(I)
\quad\text{boundedly},
}
\]

where `BV_0(I)={u in L^1(I): Eu in BV(R)}` as in `PL-301`.

More generally, for every fixed aperture `a` and every `z` in the resolvent set of the odd restriction, the same high-frequency argument rules out a bounded map `(\widetilde A^-_a-z)^{-1}:L^2_odd->BV_0`. Thus the obstruction is not the small numerical size of the certified gap. It is the logarithmic order of the principal operator.

This closes a specific shortcut for the accepted zero-order Hadamard/BV program: if an aperture derivative or derivative-measure equation is placed in the odd sector, an ordinary `L^2` estimate on its right-hand side plus the odd spectral gap cannot yield the uniform BV control needed to pass prime-shift derivatives. Any successful resolvent argument must exploit a substantially smaller, source-structured class of right-hand sides or a stronger Banach/measure coercivity than Hilbert-space invertibility.

## 1. High-frequency odd graph vectors cost only `log K`

`PL-289` identifies the principal fixed-domain operator `T` with the compression of the whole-line logarithmic multiplier

\[
m(\xi)=\log|\xi|+\gamma,
\]

and Suzuki's full operator at fixed aperture has the bounded-perturbation form

\[
\widetilde A_a=T+K_a.
\]

Choose a nonzero real even cutoff `chi in C_c^infty(I)` and set

\[
v_K(x)=\chi(x)\sin(Kx).
\]

Then `v_K` is odd, belongs to the operator core, and its `L^2` norm stays bounded above and below for all sufficiently large `K`. Its zero extension is smooth and compactly supported away from the endpoints. Writing

\[
\widehat{Ev_K}(\xi)
=\frac{1}{2i}\bigl(\widehat\chi(\xi-K)-\widehat\chi(\xi+K)\bigr),
\]

Schwartz decay of `widehat chi` gives

\[
\|m\,\widehat{Ev_K}\|_2=O(\log K).
\]

For these interior core vectors, `Tv_K` is the restriction to `I` of the whole-line multiplier applied to `Ev_K`, so

\[
\|Tv_K\|_2=O(\log K).
\]

The remainder `K_a` is bounded on `L^2`: the prime-power pieces are finitely many compressed translations, the completion term is bounded, and the scalar part is harmless. Therefore at every fixed aperture and fixed spectral parameter `z`,

\[
\boxed{
\|(\widetilde A_a-z)v_K\|_2=O(\log K).
}
\]

Parity is preserved because the prime translations occur in the symmetric `+h/-h` combination and the continuous completion kernel is reflection invariant. Thus the same estimate holds entirely inside the odd sector.

## 2. The same vectors have variation of order `K`

Because `v_K` vanishes in a neighborhood of the endpoints, its zero-extension variation is simply the integral of the absolute derivative:

\[
\operatorname{TV}(Ev_K)
=\int_I|\chi'(x)\sin(Kx)+K\chi(x)\cos(Kx)|\,dx.
\]

Periodic averaging gives

\[
\int_I|\chi(x)\cos(Kx)|\,dx
\longrightarrow
\frac{2}{\pi}\int_I|\chi(x)|\,dx>0.
\]

Hence, for some constant `c_chi>0`,

\[
\boxed{
\operatorname{TV}(Ev_K)\ge c_\chi K-O(1).
}
\]

The `L^1` part of the `BV_0` norm remains `O(1)`, so

\[
\|v_K\|_{BV_0}\asymp K
\]

from below, while the full localized-Weil graph cost is only `O(log K)`.

Equivalently, the operator-domain embedding

\[
(D(\widetilde A_a),\|u\|_2+\|\widetilde A_a u\|_2)
\hookrightarrow BV_0(I)
\]

is not continuous, even after restricting to the odd subspace.

## 3. Contradiction to any gap-only `L^2 -> BV` resolvent estimate

At `a=0.8`, let

\[
f_K=(\widetilde A^-_{0.8}-\lambda_1)v_K.
\]

The certified odd gap makes `R^-` a bounded everywhere-defined operator on odd `L^2`, and by construction

\[
R^-f_K=v_K.
\]

If the spectral gap upgraded the resolvent to a bounded map into `BV_0`, there would be a constant `C` such that

\[
\|v_K\|_{BV_0}
\le C\|f_K\|_2.
\]

The preceding estimates would force

\[
c_\chi K-O(1)\le C'\log K,
\]

which is impossible. Therefore the exact odd resolvent has no such smoothing property despite its strictly positive and explicitly certified distance from the ground level.

The proof uses only that the remainder is `L^2`-bounded. It does not replace Suzuki's source by an engineered perturbation, unlike the matched adversarial construction in `PL-300`. The failure occurs for the actual canonical localized-Weil operator at the certified compact window.

The same argument works for any `z in rho(\widetilde A^-_a)`: the high-frequency packet estimate is unchanged after subtracting a fixed scalar, so every ordinary odd `L^2` resolvent lacks `BV_0` smoothing.

## 4. Why this is a new restriction relative to `PL-300`--`PL-302`

`PL-300` shows that abstract norm-small perturbation theory, simple-gap persistence, and even uniform eigenvector convergence do not preserve BV: an engineered rank-two perturbation can inject high-frequency oscillation at logarithmically cheap spectral cost. `PL-301` then shows that Suzuki's *actual* remainder is much better behaved on BV, and `PL-302` rules out only the simplest contraction estimate for the exact finite prime comb once the `n=3` channel is active.

The present result attacks a different surviving possibility: use the actual `a=0.8` parity gap to invert a differentiated eigen-equation in the odd sector and recover variation from the `L^2` norm of its forcing. That step is impossible in this form even for the exact operator. The obstruction is intrinsic to the logarithmic principal symbol and survives all bounded source/completion terms.

This does **not** say that the actual ground state or its aperture derivative has infinite variation. It says that such control cannot be a consequence of the ordinary Hilbert-space resolvent bound alone. A special forcing may lie in a much smaller range on which stronger estimates hold.

## 5. Prior-art and novelty audit

The high-frequency mechanism is consistent with established logarithmic-Laplacian theory rather than a new generic regularity phenomenon. Chen--Weth's Dirichlet framework, already stored as source 96, identifies the Fourier symbol `2 log|xi|`; the later optimal-boundary literature stored as source 97 works at the genuinely logarithmic boundary scale rather than supplying a positive-order smoothing theorem. Recent literature searches for logarithmic-Laplacian resolvent regularity, bounded variation, and pseudodifferential/log-Sobolev mapping properties found functional and boundary regularity results but no theorem contradicting the elementary scale separation above.

No novelty is claimed for the general observation that a logarithmic-order operator cannot control a first spatial derivative on arbitrary high-frequency packets. The line-local exact contribution is the application to Suzuki's **full canonical odd sector at the certified `a=0.8` ground level**: even the explicit spectral gap from `PL-284`, combined with the exact source/completion operator, cannot provide the `L^2 -> BV` resolvent estimate that would close the current Hadamard/BV route.

No new literature entry is required. Sources 56, 58, 96, and 97 are already recorded in `research/prime_lattice/SOURCES.md` and cover the canonical localized-Weil operator, the certified compact-window parity bounds, the logarithmic principal operator, and the sharp logarithmic regularity context.

## 6. Adversarial boundaries

**No contradiction with the certified spectral gap.** The gap controls `||R^-||_{2->2}`. BV is a strictly stronger, frequency-sensitive norm, and the packet family exhibits exactly why no bound into that norm follows.

**No contradiction with all-log eigenstate regularity.** `PL-291` bootstraps actual eigenstates through every fixed logarithmic Fourier moment. The packet family consists of arbitrary graph-domain test vectors, not eigenstates. Moreover, every fixed logarithmic weight remains asymptotically weaker than the linear-frequency cost of variation.

**No statement about a structured forcing range.** A differentiated ground-state equation may produce a special commutator, boundary measure, or source-coupled forcing. The theorem excludes a proof that estimates this forcing only in ordinary `L^2` and then invokes the gap. It does not exclude an estimate in a stronger source-specific norm or a cancellation identity on that special range.

**No sign theorem.** The independent obstacle from `PL-294`--`PL-295` remains: even perfect regularity transport would still require a source-specific mechanism preventing the ground level from crossing zero.

**No regularization passage is proved or disproved.** The accepted small-order Hadamard clue also requires a controlled `s->0+` boundary-stress limit. The present result narrows only the BV/shift-derivative component.

## Consequence for `prime_lattice`

The live coupled-eigen-equation target becomes more precise. Neither the sharp finite-window parity gap nor an ordinary odd-sector resolvent norm can convert an `L^2` differentiated equation into the uniform derivative-measure estimate required by `PL-299`.

A viable continuation must therefore prove one of the genuinely stronger statements left untouched here: a resolvent/coercivity estimate in a BV or finite-measure forcing norm tailored to the exact commutator; a source-specific cancellation that removes the high-frequency packet channel; an order/variation principle for the actual ground branch; or a direct equation for its derivative measure. In particular, `spectral gap + L^2 forcing` is now a closed route, while `source-structured forcing + non-Hilbert coercivity` remains open.