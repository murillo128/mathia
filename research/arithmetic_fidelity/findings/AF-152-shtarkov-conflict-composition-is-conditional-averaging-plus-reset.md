# AF-152 — Shtarkov conflict composition is conditional averaging plus reset

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `QUANTITATIVE-FIDELITY`, `POSITIVE-STABILITY-CRITERION`, `NO-NOVELTY-CLAIM`

## Claim

AF-151 identified the one-step drift between a propagated Shtarkov center and the center recomputed after compression with the normalized local max-sum conflict profile. For a chain of compressions, those one-step conflicts do **not** multiply pointwise. The exact composition law alternates two operations:

1. conditional averaging of all previously accumulated conflict through the current channel; and
2. multiplication by the current local recanonicalization/reset density.

This yields an additive strong-divergence budget for moving Shtarkov centers. The relevant stage cost is the local reset drift `D_∞(M_{j-1}K_j || M_j)`, not the scalar maximal-leakage drop `log(C_{j-1}/C_j)`.

Let

\[
\mathcal E_0=(P_i^{(0)})_{i=1}^m
\]

be a finite experiment on a finite set `X_0`, and let

\[
X_0\xrightarrow{K_1}X_1\xrightarrow{K_2}\cdots
\xrightarrow{K_n}X_n
\tag{1}
\]

be stochastic channels. Write

\[
P_i^{(j)}=P_i^{(0)}K_1\cdots K_j,
\qquad
s_j(x)=\max_iP_i^{(j)}(x),
\qquad
C_j=\sum_x s_j(x),
\tag{2}
\]

and let

\[
M_j(x)=\frac{s_j(x)}{C_j}
\tag{3}
\]

be the Shtarkov/NML center of the stage-`j` experiment.

For one step define

\[
R_j:=M_{j-1}K_j,
\tag{4}
\]

and the AF-151 local conflict factor

\[
\kappa_j(y)
:=
\frac{\sum_x s_{j-1}(x)K_j(y\mid x)}{s_j(y)}.
\tag{5}
\]

The laws `R_j` and `M_j` have the same support. With

\[
\mu_j:=\frac{C_{j-1}}{C_j}
=\mathbb E_{M_j}\kappa_j,
\tag{6}
\]

AF-151 gives the exact reset density

\[
\boxed{
\rho_j(y):=\frac{dR_j}{dM_j}(y)
=\frac{\kappa_j(y)}{\mu_j}.
}
\tag{7}
\]

Now propagate the **original** center without recanonicalizing:

\[
q_j:=M_0K_1\cdots K_j,
\qquad
h_j:=\frac{dq_j}{dM_j},
\qquad
h_0\equiv1.
\tag{8}
\]

Define the reverse/Bayes kernel associated with the local reference transition `M_{j-1} -> R_j` by

\[
B_j(x\mid y)
:=
\frac{M_{j-1}(x)K_j(y\mid x)}{R_j(y)}
\tag{9}
\]

on the common support. Then the accumulated density obeys the exact recursion

\[
\boxed{
h_j(y)
=\rho_j(y)\,(B_jh_{j-1})(y).
}
\tag{10}
\]

Equivalently,

\[
(B_jh)(y)
=\mathbb E[h(X_{j-1})\mid X_j=y]
\tag{11}
\]

under `X_{j-1}~M_{j-1}` and `X_j|X_{j-1}~K_j`. Thus old mismatch is first averaged over the source states made indistinguishable at the new output, after which the newly recomputed Shtarkov center contributes the multiplicative reset `rho_j`.

There is an equally exact unnormalized conflict recursion. Put

\[
\widetilde s_{0\to j}:=s_0K_1\cdots K_j,
\qquad
\kappa_{0\to j}:=\frac{\widetilde s_{0\to j}}{s_j}.
\tag{12}
\]

Since

\[
\frac{C_0}{C_j}=\prod_{r=1}^j\mu_r,
\qquad
h_j=\frac{\kappa_{0\to j}}{C_0/C_j},
\tag{13}
\]

formula `(10)` is equivalent to

\[
\boxed{
\kappa_{0\to j}
=\kappa_j\,B_j\kappa_{0\to j-1}.
}
\tag{14}
\]

For two stages this reads

\[
\boxed{
\kappa_{0\to2}(z)
=\kappa_2(z)\,
\mathbb E_{B_2}[\kappa_1(Y)\mid Z=z].
}
\tag{15}
\]

So local conflict is **not** a pointwise multiplicative cocycle. Its composition law is multiplication only after a channel-dependent conditional-expectation projection.

## Strong-divergence composition budget

For every `p in (1,infinity)`, `(10)` and conditional Jensen give

\[
\begin{aligned}
\|h_j\|_{L^p(M_j)}^p
&=\int \rho_j^p|B_jh_{j-1}|^p\,dM_j\\
&=\int \rho_j^{p-1}|B_jh_{j-1}|^p\,dR_j\\
&\le \|\rho_j\|_\infty^{p-1}
   \int |B_jh_{j-1}|^p\,dR_j\\
&\le \|\rho_j\|_\infty^{p-1}
   \int |h_{j-1}|^p\,dM_{j-1}.
\end{aligned}
\tag{16}
\]

Hence

\[
\boxed{
D_p(q_j\|M_j)
\le
D_p(q_{j-1}\|M_{j-1})
+
D_\infty(R_j\|M_j),
}
\tag{17}
\]

where

\[
D_\infty(R_j\|M_j)
=\log\|\rho_j\|_\infty
=\log\operatorname*{ess\,sup}_{M_j}
\frac{\kappa_j}{\mu_j}.
\tag{18}
\]

The same inequality holds for `p=infinity` directly from `(10)`. Iterating from `q_0=M_0` gives

\[
\boxed{
D_p(M_0K_1\cdots K_n\|M_n)
\le
\sum_{j=1}^n
D_\infty(M_{j-1}K_j\|M_j),
\qquad 1<p\le\infty.
}
\tag{19}
\]

The KL endpoint obeys the same reset budget. Since `q_j=q_{j-1}K_j`, data processing gives

\[
D_{\rm KL}(q_j\|R_j)
\le
D_{\rm KL}(q_{j-1}\|M_{j-1}).
\tag{20}
\]

Moreover,

\[
\begin{aligned}
D_{\rm KL}(q_j\|M_j)
&=D_{\rm KL}(q_j\|R_j)
  +\mathbb E_{q_j}\log\rho_j\\
&\le D_{\rm KL}(q_j\|R_j)
  +\log\|\rho_j\|_\infty.
\end{aligned}
\tag{21}
\]

Therefore

\[
\boxed{
D_{\rm KL}(M_0K_1\cdots K_n\|M_n)
\le
\sum_{j=1}^n D_\infty(M_{j-1}K_j\|M_j).
}
\tag{22}
\]

Total variation has the analogous metric form

\[
\boxed{
\|q_n-M_n\|_{\rm TV}
\le
\sum_{j=1}^n\|M_{j-1}K_j-M_j\|_{\rm TV},
}
\tag{23}
\]

by data processing plus the triangle inequality.

Equations `(19)` and `(22)` are **sufficient stability budgets**, not identities and not necessary conditions. They quantify the cumulative price of repeatedly forgetting provenance and then selecting a fresh canonical center.

## Separating controls

### Scalar maximal-leakage loss is the wrong strong stage budget

AF-150 showed that the scalar quantities

\[
\log\mu_j=\log\frac{C_{j-1}}{C_j}
\tag{24}
\]

telescope exactly. AF-151 then exhibited the private-label family at scale `rho=m^{-2}` for which

\[
\log\mu_j\longrightarrow0
\tag{25}
\]

while

\[
D_\infty(R_j\|M_j)
\sim\log m.
\tag{26}
\]

Thus even a vanishing scalar maximal-leakage drop can coexist with divergent strong local recanonicalization drift. Replacing the right-hand side of `(19)` or `(22)` by the telescoping scalar loss is therefore impossible without an additional tail/dispersion hypothesis on `kappa_j`.

The distinction is structural. `log mu_j` sees only the mean conflict `E_{M_j} kappa_j`; the strong reset cost sees the largest normalized local conflict `kappa_j/mu_j`.

### Later coarse-graining can erase earlier reset drift completely

The additive budget is deliberately one-sided and conservative. Start with any first step for which

\[
h_1\ne1.
\tag{27}
\]

Let the next channel `K_2` send every point of `X_1` to a single output `*`. Then every compressed experiment law is `delta_*`, so

\[
M_2=R_2=q_2=\delta_*,
\qquad
\rho_2\equiv1.
\tag{28}
\]

The reverse kernel at the singleton output is simply `M_1`, hence

\[
(B_2h_1)(*)
=\mathbb E_{M_1}h_1
=1.
\tag{29}
\]

Equation `(10)` gives `h_2=1`: the endpoint drift is exactly zero even though stage 1 may have had a large reset cost. Conditional averaging has destroyed the earlier mismatch.

Therefore no lower bound on endpoint drift can depend only monotonically on the sum of the stagewise reset costs. A useful composition theory must remember **both** local recanonicalization and how subsequent channels contract the accumulated density profile.

## Prior art and novelty assessment

The ingredients used above are classical.

- Yuri M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175–186 (1987), is the classical source for the normalized maximum-likelihood/Shtarkov law and minimax pointwise regret.
- Ibrahim Issa, Aaron B. Wagner, and Sudeep Kamath, **“An Operational Approach to Information Leakage,”** *IEEE Transactions on Information Theory* 66(3), 1625–1657 (2020), DOI `10.1109/TIT.2019.2962804`, identifies maximal leakage with Sibson mutual information of order infinity, gives the discrete max-sum formula, and establishes its data processing.
- Baris Nakiboglu, **“The Renyi Capacity and Center,”** *IEEE Transactions on Information Theory* 65(2), 841–860 (2019), DOI `10.1109/TIT.2018.2861002`, gives the general Renyi capacity/radius/center framework in which the finite order-infinity Shtarkov center sits.
- Tim van Erven and Peter Harremoes, **“Renyi Divergence and Kullback-Leibler Divergence,”** *IEEE Transactions on Information Theory* 60(7), 3797–3820 (2014), DOI `10.1109/TIT.2014.2320500`, arXiv:`1206.2459`, is an authoritative source for classical Renyi-divergence properties including data processing and minimax information-radius results.
- Jason M. Altschuler and Sinho Chewi, **“Shifted Composition III: Local Error Framework for KL Divergence,”** *Foundations of Computational Mathematics* (2026), DOI `10.1007/s10208-026-09753-x`, develops a modern local-error/composition framework and records Renyi composition and weak-triangle tools in its appendix. This is neighboring general divergence-composition prior art, not a Shtarkov-specific source.

The density-under-a-Markov-map identity behind `(10)` is standard change-of-measure/conditional-expectation mathematics, and the divergence bounds `(17)--(23)` are direct consequences of standard data processing, Jensen/Hölder-type estimates, and an intermediate-reference `D_infinity` bound. **No novelty is claimed for those general probabilistic or information-theoretic facts.**

A targeted search did not locate a source stating the exact Shtarkov specialization `(14)`: the stagewise max-sum conflict profile from AF-151 is conditionally averaged by the Bayes reverse kernel of the moving NML reference and then multiplied by the next local conflict. That specialization is recorded here as a derived organizing identity, not as a novelty claim.

## Boundary conditions and audit

The theorem is finite and support-sensitive. The common-support statement for `R_j` and `M_j` follows because `M_{j-1}` is positive exactly on the union of supports of the stage-`j-1` experiment family: an output is reachable from `M_{j-1}` through `K_j` iff it is reachable from at least one `P_i^{(j-1)}`, which is iff the new envelope `s_j` is positive there.

The exact recursion requires the reference at every stage to be the **recomputed Shtarkov center of the current experiment**. Choosing an unrelated moving reference changes `rho_j`; choosing a fixed reference removes the recanonicalization mechanism being studied. The additive divergence bounds are directional: they control the source-propagated law relative to the recomputed current center. Reverse likelihood-ratio drift can require a separate lower-tail bound on the density.

The finite proof does not by itself establish an infinite-alphabet or continuous-model theorem. Such an extension would require existence/normalizability of the relevant Shtarkov centers, absolute-continuity control, and the corresponding conditional-expectation machinery.

## Consequence for Arithmetic Fidelity

AF-150 supplied a telescoping **scalar** information-loss budget; AF-151 exposed the **local** conflict profile hidden behind that scalar. The present result gives the missing composition law:

\[
\boxed{
\text{old mismatch}
\xrightarrow{\text{conditional averaging}}
\text{surviving mismatch}
\xrightarrow{\text{local reset}}
\text{new mismatch}.
}
\tag{30}
\]

This is a concrete answer to the line's composition question. Canonical compression can forget an earlier defect, while recanonicalization can inject a new one. Consequently, preservation through a long pipeline cannot be audited only by summing coarse information losses or by checking each endpoint independently. A strong fidelity certificate needs a stagewise reset profile together with the contraction induced by the intervening channels.

For later prime-specific applications this gives a precise gate: if a proposed prime-derived pipeline repeatedly canonicalizes after quotienting, averaging, spectralization, or another compression, the relevant question is whether the arithmetic discriminator's accumulated likelihood profile is contracted by the next map faster than the next canonical reset can amplify it. The theorem does not supply such a prime discriminator; it specifies the exact abstract mechanism that any such argument would have to control.