# MC-354 — Log-smooth additive readout converts source-edge geometry into a Jeffreys tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-351`–`MC-353` reduce the current reciprocal-endpoint bottleneck to a concrete statistical question: bounded-energy dephasing forces a constant average Jeffreys/privacy-loss budget on natural source edges, but a useful analytic architecture needs an independent way to upper-price that budget from its actual resources.

A broad additive-noise readout supplies such a price. Let the source state be `X`, let

\[
T=\Phi(X)\in\mathbb R^d,
\qquad
Z=T+N,
\tag{1}
\]

where `N` is independent of `X` and has everywhere-positive density `q` on `R^d`. Assume the complete admitted coefficient observation `Y` is downstream of this readout,

\[
X\longrightarrow T\longrightarrow Z\longrightarrow Y.
\tag{2}
\]

Write

\[
f=\log q,
\qquad
S(n)=\nabla f(n).
\tag{3}
\]

Assume:

1. `f` is continuously differentiable and its score is globally `beta`-Lipschitz,
   \[
   \|S(u)-S(v)\|_2\le\beta\|u-v\|_2;
   \tag{4}
   \]
2. `S(N)` is integrable and the usual boundary condition holds so that
   \[
   \mathbf E S(N)=0.
   \tag{5}
   \]

For a natural source edge `e={x,x'}`, put

\[
h_e:=\Phi(x')-\Phi(x).
\tag{6}
\]

Let `P_e,Q_e` be the complete transcript laws conditioned on the two endpoints and let

\[
b_e:=\frac12\left(D(P_e\|Q_e)+D(Q_e\|P_e)\right)
\tag{7}
\]

be the half-Jeffreys edge divergence used in `MC-348`–`MC-353`. Then

\[
\boxed{
 b_e\le \frac\beta2\|h_e\|_2^2.
}
\tag{8}
\]

Thus the previously insufficient **forward source-edge displacement** becomes a valid reverse-discrimination currency once the readout channel has explicit log-density curvature.

Choose a natural source edge uniformly and define

\[
G_{2,R}^2:=\mathbf E_e\|h_e\|_2^2.
\tag{9}
\]

`MC-353` proves that under bounded coefficient energy and fixed nontrivial dephasing,

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad C<\infty,\ \eta>0,
\tag{10}
\]

one has, for either parity,

\[
\mathbf E_e b_e
\ge
\frac{\eta^2}{C}-o(1).
\tag{11}
\]

Combining `(8)` and `(11)` gives the necessary tariff

\[
\boxed{
\frac{\beta_R}{2}G_{2,R}^2
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{12}
\]

Equivalently,

\[
\boxed{
\beta_R G_{2,R}^2
\ge
\frac{2\eta^2}{C}-o(1).
}
\tag{13}
\]

Therefore any additive-readout architecture satisfying

\[
\beta_R G_{2,R}^2\longrightarrow0
\tag{14}
\]

cannot sustain fixed nontrivial dephasing at bounded coefficient energy. The architecture must pay either through nonvanishing source-edge motion, increasingly sharp/noiseless readout curvature, or growing coefficient energy.

There is also a direct privacy-loss moment form. For `p>1`, define

\[
s_{p,R}:=\left(\mathbf E\|S(N)\|_2^p\right)^{1/p},
\qquad
G_{p,R}:=\left(\mathbf E_e\|h_e\|_2^p\right)^{1/p}.
\tag{15}
\]

Let `U_R` be the absolute source-edge privacy loss under the edge-mixture experiment of `MC-353`. Then

\[
\boxed{
\left(\mathbf E U_R^p\right)^{1/p}
\le
s_{p,R}G_{p,R}
+\frac{\beta_R}{2}G_{2p,R}^2.
}
\tag{16}
\]

Since `MC-353` gives

\[
\mathbf E\psi(U_R)
\ge
\frac{\eta^2}{C}-o(1),
\qquad
\psi(u)=u\tanh(u/2)\le u,
\tag{17}
\]

fixed bounded-energy dephasing also forces

\[
\boxed{
 s_{p,R}G_{p,R}
+\frac{\beta_R}{2}G_{2p,R}^2
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{18}
\]

Thus the rare-event loophole isolated in `MC-353` can be closed by a concrete combination of **score moments** and **source-edge displacement moments**. No essential-supremum likelihood-ratio bound is required.

For isotropic Gaussian noise `N~N(0,sigma^2 I_d)`, `beta=1/sigma^2` and `(8)` is exact:

\[
b_e=\frac{\|h_e\|_2^2}{2\sigma^2}.
\tag{19}
\]

So the theorem recovers the correct inverse-resolution currency of `MC-343` locally on the source graph, rather than through global channel capacity.

No estimate for `M(x)` follows. The advance is a finite reciprocal-endpoint admission theorem: an actual analytic architecture with additive log-smooth readout must now defeat an explicit product of forward source motion and reverse readout curvature.

## 1. Log-smooth noise gives a quadratic shift-KL bound

Fix two deterministic transcript points `a,b` and write

\[
h=b-a.
\]

Before the downstream channel in `(2)`, the two noisy-readout laws have densities

\[
p_a(z)=q(z-a),
\qquad
p_b(z)=q(z-b).
\tag{20}
\]

Under `p_a`, write `z=a+N`. The log-likelihood ratio is

\[
L_{a,b}(z)
=f(N)-f(N-h).
\tag{21}
\]

The Lipschitz-gradient assumption `(4)` gives the two-sided descent estimate

\[
\left|
 f(N-h)-f(N)+\langle S(N),h\rangle
\right|
\le
\frac\beta2\|h\|_2^2.
\tag{22}
\]

Hence

\[
L_{a,b}(a+N)
\le
\langle S(N),h\rangle
+\frac\beta2\|h\|_2^2.
\tag{23}
\]

Taking expectation and using `(5)` yields

\[
D(p_a\|p_b)
\le
\frac\beta2\|h\|_2^2.
\tag{24}
\]

Interchanging `a,b` gives the same bound in the reverse direction. Therefore

\[
\frac12\bigl(D(p_a\|p_b)+D(p_b\|p_a)\bigr)
\le
\frac\beta2\|h\|_2^2.
\tag{25}
\]

Finally the complete admitted observation `Y` is obtained from `Z` by a common Markov kernel. KL data processing applies in both directions, proving `(8)`.

The score-centering condition `(5)` is load-bearing only in the first-order term. For ordinary smooth probability densities decaying sufficiently at infinity it follows from integration by parts,

\[
\mathbf E S(N)
=\int \nabla q(n)\,dn=0.
\]

It is stated explicitly so that no boundary regularity is hidden in the theorem.

## 2. MC-353 turns the local shift bound into a dephasing resource inequality

`MC-353` already normalized the even Hamming-edge source and the odd parity-preserving pair-edge source so that the per-edge lower tariff has the same asymptotic constant:

\[
\overline b_R
:=\mathbf E_e b_e
\ge
\frac{\eta^2}{C}-o(1)
\tag{26}
\]

under `(10)`. Averaging `(8)` over the same natural edge law gives

\[
\overline b_R
\le
\frac{\beta_R}{2}
\mathbf E_e\|h_e\|_2^2
=
\frac{\beta_R}{2}G_{2,R}^2.
\tag{27}
\]

Equations `(26)`–`(27)` prove `(12)`–`(13)`.

This exposes the missing inverse-conditioning factor precisely. `MC-342` showed that a deterministic scalar encoding may have bounded range and tiny edge displacements while still retaining the entire source in exponentially fine digits. Such an encoding has no statistical penalty when every distinct real number is read with infinite precision. Under additive log-smooth noise, the same tiny displacement can distinguish neighboring source states only in proportion to `beta ||h||^2`; shrinking the noise scale makes `beta` grow and records the hidden inverse precision explicitly.

The theorem therefore does not rehabilitate generic forward Lipschitz control. It says that forward geometry becomes useful only after composition with a readout whose reverse statistical conditioning is quantitatively declared.

## 3. Score moments upper-price the entire privacy-loss tail

The same descent estimate gives more than mean KL. Under the first endpoint law,

\[
|L_{a,b}(a+N)|
\le
\|S(N)\|_2\,\|h\|_2
+\frac\beta2\|h\|_2^2.
\tag{28}
\]

Under the second endpoint law, writing `z=b+N`, the privacy loss `log(p_a/p_b)` equals `f(N+h)-f(N)` and satisfies the identical absolute bound. Therefore, after choosing an edge uniformly and then drawing from the endpoint mixture used in `MC-353`, Minkowski's inequality gives

\[
\begin{aligned}
B_{p,R}
&:=\left(\mathbf E U_R^p\right)^{1/p}\\
&\le
\left(
\mathbf E\bigl[\|S(N)\|_2\|h_e\|_2\bigr]^p
\right)^{1/p}
+
\frac\beta2
\left(\mathbf E\|h_e\|_2^{2p}\right)^{1/p}\\
&=
s_{p,R}G_{p,R}
+\frac{\beta_R}{2}G_{2p,R}^2.
\end{aligned}
\tag{29}
\]

The factorization in the first term uses independence between the sampled source edge and the additive readout noise. This proves `(16)`.

Since the edge-mixture experiment is a probability law and `p>1`,

\[
\mathbf E\psi(U_R)
\le
\mathbf E U_R
\le
B_{p,R}.
\tag{30}
\]

Combining `(30)` with the lower tariff `(17)` proves `(18)`.

This is stronger than merely assuming `U_R->0` in probability. The score/displacement estimate controls an actual moment of the privacy loss, hence gives the uniform-integrability currency that `MC-353` identified as sufficient to eliminate rare, arbitrarily decisive transcript events.

## 4. Gaussian noise is the sharp calibration case

For

\[
q(n)
=(2\pi\sigma^2)^{-d/2}
\exp\left(-\frac{\|n\|_2^2}{2\sigma^2}\right),
\]

one has

\[
S(n)=-\frac n{\sigma^2},
\qquad
\|S(u)-S(v)\|_2
=\frac1{\sigma^2}\|u-v\|_2,
\tag{31}
\]

so `beta=1/sigma^2`. Two equal-covariance Gaussian shifts satisfy

\[
D(p_a\|p_b)
=D(p_b\|p_a)
=\frac{\|a-b\|_2^2}{2\sigma^2},
\tag{32}
\]

and hence `(8)` is equality.

This calibration separates the present theorem from `MC-343`. `MC-343` prices **global transcript capacity** using Gaussian maximum entropy and total signal-to-noise spread. The present result prices the **local source-edge Jeffreys and privacy-loss budgets** that emerged only later in `MC-351`–`MC-353`, and it applies to every additive positive density with Lipschitz score, not only to Gaussian readout.

The two statements are compatible but answer different questions. A high-dimensional transcript could have large global capacity while neighboring source rows remain statistically close; conversely, a small set of expensive edges could have large local divergence without maximizing global AWGN capacity. The current edge tariff is the quantity directly demanded by the source-graph converse.

## 5. Prior art and novelty boundary

No novelty is claimed for the information-theoretic ingredients. Shift divergences of additive-noise mechanisms, likelihood/privacy-loss variables, KL data processing, score functions, and smooth-log-density estimates are classical or standard tools across information theory, privacy, and sampling.

A targeted prior-art audit on 17 September 2026 found particularly close modern shift-reduction machinery in:

- Rémi Pierquin, Aurélien Bellet, Marc Tommasi and Catuscia Palamidessi Boussard, *Rényi Pufferfish Privacy: General Additive Noise Mechanisms and Privacy Amplification by Iteration via Shift Reduction Lemmas*, Proceedings of Machine Learning Research 235 (ICML 2024), 40762–40794, https://proceedings.mlr.press/v235/pierquin24a.html, arXiv `2312.13985`. The paper develops additive-noise privacy guarantees for broad noise classes through shift-reduction/divergence techniques.
- The privacy-loss and Rényi-divergence literature already cited in `MC-353`, including Mironov's Rényi differential privacy and concentrated-DP work, supplies the standard moment/tail viewpoint. The present finding does not claim the score-moment privacy-loss bound as a new general privacy theorem.

The elementary proof `(21)`–`(25)` is included because it fixes exactly the normalization needed by the Mathia half-Jeffreys edge budget. The durable Mathia-specific delta is the composition with `MC-351`/`MC-353`: the lower tariff forced by reciprocal-source dephasing and the upper tariff supplied by an admitted additive readout now meet in the explicit resource products `(12)` and `(18)`.

No claim is made that this composition is new outside this research program, and no arithmetic consequence is inferred without proving that a natural Möbius/endpoint architecture actually factors through a readout satisfying these hypotheses.

## 6. Boundaries and falsification tests

- **The complete admitted transcript must factor through the noisy readout.** If the architecture exposes any side channel carrying source information outside `Z`, KL data processing does not upper-bound the complete transcript by `(8)`.
- **Positivity/common support is structural.** If `q` vanishes or has compact support, shifted rows may acquire singular pieces and infinite KL. That is not a technical nuisance: it is exactly the rare-event/singularity escape route isolated by `MC-352`–`MC-353`.
- **Global score Lipschitzness is sufficient, not necessary.** An architecture may admit sharper direct shift-KL or Rényi estimates without a finite global `beta`. Failure of `(4)` does not establish that dephasing is possible.
- **Score centering must be justified.** Heavy tails or irregular boundaries can invalidate the integration-by-parts shortcut; `(5)` is therefore an explicit hypothesis.
- **Shrinking noise is not free.** If the readout scale tends to zero, `beta_R` and typically `s_{p,R}` diverge. Equations `(13)` and `(18)` record that inverse precision rather than hiding it in the real-valued encoding.
- **Large source-edge motion is necessary, not sufficient.** Paying the lower tariff does not produce useful Möbius cancellation; it only avoids this admission obstruction.
- **Average geometry is the relevant normalization.** A few very long edges may carry the required budget. Any stronger conclusion about uniform edge motion would need an additional concentration or maximum-edge hypothesis.
- **The p-moment theorem does not require a worst-case likelihood ceiling.** It is deliberately weaker than `MC-352`; rare large privacy losses are permitted as long as their moment cost is paid through score and displacement moments.
- **This remains finite-source mathematics.** Nothing here proves a bound on `M(x)`, a zero-free half-plane, or an RH-scale cancellation theorem.

## Research consequence

The frontier no longer needs an abstract request to “upper-bound privacy-loss tails.” For additive-readout architectures there is now a concrete admissibility test:

\[
\beta_R G_{2,R}^2
\not\to0,
\tag{33}
\]

and, more strongly for any available `p>1`,

\[
s_{p,R}G_{p,R}
+\frac{\beta_R}{2}G_{2p,R}^2
\not\to0
\tag{34}
\]

under fixed bounded-energy dephasing.

The next arithmetic step is therefore sharply separated from the information-theory layer: construct or rule out a **natural Möbius/endpoint transcript** whose source-edge displacement moments can be estimated, identify the actual readout/regularization that makes those distinctions observable, and compare the resulting `beta`, score moments, and precision scale with the forced tariffs above. If every natural construction has `beta_R G_{2,R}^2=o(1)`, bounded-energy dephasing is excluded; if not, the surviving architecture has exposed exactly where its inverse-resolution resource lives.