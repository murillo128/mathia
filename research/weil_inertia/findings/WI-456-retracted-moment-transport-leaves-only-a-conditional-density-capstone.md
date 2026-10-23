# WI-456 — retracted arithmetic transport leaves a conditional density capstone

**Status:** PRIMARY-SOURCE-CORRECTION + EXACT-CONDITIONAL + CLASSICAL-MOMENT-METHOD + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** WI-001 (the independently established baseline and counting budget), WI-003 (the separate literal cell-cutoff obstruction), WI-006 (screened off-line/double replacement).

## Source correction and exact evidence boundary

The Yang--Yang unconditional higher-moment program is **retracted**, rather than a currently certified candidate awaiting its first audit. Its official [retraction notice](https://github.com/JoshuaHKU/zeta-density-one-reproduction/blob/ac851520f1d135a56d2911ff512011feab2a32dd/RETRACTION.md), at revision `ac851520f1d135a56d2911ff512011feab2a32dd`, withdraws the unconditional higher-even-moment tier beginning with \(\mu_4\to13/4\) and the density-one consequences. The notice on the source's default branch has the same Git blob, `61a7b8d0ce377ce6ba81ffa05dee085104c96801`.

Consequently neither the fourth-moment rung nor the later `79.62%`, order-14, or density-one conclusions can enter Mathia as unconditional evidence through this program. Exact rational calculations, model moments, finite certificates, and Lean artifacts establish only their own checked statements; they cannot restore the withdrawn analytic transport.

The notice attributes the failure to an essential gap and reports a review argument called Proposition R. It does not contain that argument's precise hypotheses or proof. Its assertion that sufficiently strong higher-even-moment bounds would imply power-law zero-free regions is **a source report, not a theorem independently established here**. The notice does not prove that every possible higher-moment theorem is false or that a genuinely new arithmetic proof is impossible. It explicitly preserves the independent Alpöge--Furman baseline. Its references to later conditional work supply no unconditional substitute.

The affirmative assessment that this particular submitted proof remains a live candidate is withdrawn. The useful mathematical content to retain is the separation between arithmetic moment input, model determinacy/zero-atom control, and the final counting implication. The following sufficient conditional statement makes those layers explicit without relying on the retracted source.

## An independently reconstructed sufficient moment-to-density theorem

For each parameter \(T\), let \(A_T\) be a Hermitian matrix of dimension \(d_T\), and let \(N_T\to\infty\) with \(d_T/N_T\to1\). Put
\[
\mu_T=\frac1{d_T}\sum_{j=1}^{d_T}\delta_{\lambda_j(A_T)}.
\]
Assume all of the following:

1. For every **fixed** integer \(r\ge0\),
   \[
   \int x^r\,d\mu_T(x)\longrightarrow m_r=\int x^r\,d\nu(x),
   \tag{1}
   \]
   where \(\nu\) is a Borel probability measure with all moments finite.
2. \(\nu\) is determinate for the **Hamburger** moment problem: it is the unique probability measure on \(\mathbb R\) with moments \((m_r)\). Also \(\nu(( -\infty,0])=0\).
3. The actual source supplies the positive-index counting bound
   \[
   n_+(A_T)\le \frac{N_T+S_T}{2}+o(N_T),
   \qquad 0\le S_T\le N_T.
   \tag{2}
   \]

Then
\[
\boxed{n_{\le0}(A_T)=o(N_T),\qquad S_T/N_T\longrightarrow1.}
\tag{3}
\]
Here \(S_T\) represents simple critical-line zeros only when (2) has actually been established for that zero population and that matrix. This is a sufficient abstract theorem, not an assertion that the withdrawn model or the zeta matrices meet its hypotheses.

**Proof of the measure step.** The bounded second moments in (1) make \(\{\mu_T\}\) tight. Along any weakly convergent subsequence, let the limit be \(\eta\). For a fixed \(r\ge1\), choose an even integer \(2s>r\). The convergent \(2s\)-moments give
\[
\int_{|x|>R}|x|^r\,d\mu_T(x)
\le R^{r-2s}\int |x|^{2s}\,d\mu_T(x)
\le C_sR^{r-2s}.
\tag{4}
\]
The same bound for \(\eta\) follows by lower semicontinuity of the higher moment. Bounded continuous cutoffs, weak convergence, and (4) show that \(\eta\) has every moment \(m_r\). Hamburger determinacy forces \(\eta=\nu\), so the whole family converges weakly to \(\nu\). The closed-set inequality for \(( -\infty,0]\) now yields
\[
\limsup_T\frac{n_{\le0}(A_T)}{d_T}
=\limsup_T\mu_T(( -\infty,0])
\le\nu(( -\infty,0])=0.
\tag{5}
\]
Thus \(n_+(A_T)=N_T-o(N_T)\). Substituting in (2) proves (3).

**Meaning of the counting input.** In an exact finite zero-block decomposition, let \(S\) count simple critical zeros, let \(c\) count distinct multiple critical points with multiplicities \(m_i\ge2\), and let \(p\) count mirror pairs with multiplicity. Critical points contribute at most one positive direction each and an off-line pair contributes at most one. Therefore
\[
n_+(A)\le S+c+p
\le S+\frac{\sum_i m_i+2p}{2}
=\frac{N+S}{2}.
\tag{6}
\]
This follows from subadditivity of positive index under addition of Hermitian forms and remains true when compression lowers a block's rank. Applying (6) to an actual truncated zeta form still requires its correct normalization and tail treatment. A small norm perturbation alone does not preserve inertia near zero; (2), including its negligible counting error, is a separate source obligation.

## Fixed order is enough for the limit, but not a substitute for input

The proof chooses each moment order before taking \(T\to\infty\); it needs no uniform rate in the order. Separately, if an independently proved certificate already gives
\[
\liminf_T S_T/N_T\ge1-2\lambda_k\quad\hbox{for every fixed }k,
\qquad \lambda_k\downarrow0,
\tag{7}
\]
then for any \(\epsilon>0\), choose a fixed \(k\) with \(2\lambda_k<\epsilon\). The single liminf is at least \(1-\epsilon\), hence equals one. This is a supremum of valid bounds on one number, not an exchange of two limits.

For a measure \(\nu\), the standard Christoffel quantity is
\[
\lambda_k(0;\nu)=\inf_{\deg q\le k,\ q(0)=1}\int |q(x)|^2\,d\nu(x).
\tag{8}
\]
The classical variational principle explains the polynomial certificate, but neither (8) nor an exact computation of model moments proves the arithmetic bounds in (1) or (7). Likewise, vanishing normalized matrix nullity alone would not control negative index: (5) controls the whole nonpositive half-line. A positive model needs independently justified determinacy and no atom at zero, as well as a valid transfer to the actual matrices. In (1)--(5) uniqueness is explicitly on \(\mathbb R\); no unspecified Stieltjes-to-Hamburger passage is assumed for an indefinite matrix family.

## Falsification controls and consequences

- If the model has an atom at zero, (5) permits that much limiting nonpositive mass. Nonnegative model support alone is insufficient.
- If only finitely many moments are available, the subsequential limit need not be determined. The first-two-moment extremizers in WI-001 remain admissible.
- If only model or finite-algebra certificates are known, premise (1) for the actual arithmetic matrices is absent. This is exactly the layer withdrawn by the source.
- WI-006's screened replacement concerns distinguishing two populations with the same compressed operator. It does not contradict a hypothetical source theorem excluding their common spectral distribution.
- Even (3) for actual zeta zeros gives density one, not RH. A finite or zero-density off-line exceptional set may remain; simplicity is a separate condition that RH does not require.

An exact control for the last limitation is \(A_d=\operatorname{diag}(-1,1,\ldots,1)\), \(N_d=d\), \(S_d=d-2\), for \(d\ge2\). Its empirical moments converge at every fixed order to those of \(\delta_1\), which is determinate and has no zero atom, and its positive-index budget is an equality. Nevertheless it has one negative direction at every \(d\). This is a finite-matrix control, not an asserted zeta-zero configuration: it shows why the conditional density theorem cannot by itself exclude every exceptional block.

The valid cell-cutoff obstruction in WI-003 remains a statement about the pinned manuscripts: a global parameter cannot implement a cellwise modulus truncation. It neither establishes the separately reported Proposition R nor turns the withdrawn proof into an active unconditional input. A future higher-moment route must provide new arithmetic transport or a new independently justified counting interface; repairing a symbol or rechecking the rational constants does not do so.

## Prior art and mathematical delta

The official source notice establishes the withdrawal. The moment method, tightness/uniform-integrability argument, and closed-set weak-convergence inequality are classical; their complete application is proved above. Barry Simon, *The Christoffel--Darboux Kernel*, [arXiv:0806.1528](https://arxiv.org/abs/0806.1528), Section 9, Theorem 9.2, supplies the classical variational principle in (8). WI-001 supplies the independent inertia/counting context. No new moment theorem, zero-density theorem, or proof of Proposition R is claimed.

The substantive correction removes the obsolete live-candidate assessment and prevents retracted analytic claims from reentering the evidence base, while preserving the precise conditional mathematics that survives. The arithmetic transfer remains the missing premise; a valid fixed-order tower would not additionally need uniformity in its order to yield density one.
