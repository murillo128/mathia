# AF-114 — Pairwise log-ratio tightness exactly classifies single-scale spectral repairability

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CONCENTRATION-COMPACTNESS`, `SCALE-FREE-FIDELITY-GATE`, `MULTISCALE-OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a complex separable Hilbert space, let

\[
1\le p<\infty,
\]

and let `(A_i)` be a net of nonzero positive operators in `\mathcal S_p(H)`. Write the positive eigenvalues of `A_i`, repeated with multiplicity, as `(\lambda_{ij})_j`, and let

\[
M_i:=\operatorname{Tr}(A_i^p)=\sum_j\lambda_{ij}^p>0.
\tag{1}
\]

AF-113 studied the particular blow-up scale `\|A_i\|` and showed that even this canonical scale can follow a negligible spectral spike while order-one `p`-mass lives at a much smaller scale. The next question is more intrinsic:

> **Is the failure caused only by a bad choice of scalar scale, or is the spectral mass genuinely too multiscale for every single scalar blow-up?**

This has an exact scale-free answer.

Define the logarithmic `p`-mass probability measure

\[
\rho_i
:=
\frac1{M_i}
\sum_j\lambda_{ij}^p\,\delta_{\log\lambda_{ij}}
\qquad\text{on }\mathbb R.
\tag{2}
\]

For two independent samples `X_i,Y_i` with law `\rho_i`, define the self-difference law

\[
\Delta_i
:=
(x-y)_\#(\rho_i\otimes\rho_i).
\tag{3}
\]

Equivalently,

\[
\Delta_i
=
\frac1{M_i^2}
\sum_{j,k}
\lambda_{ij}^p\lambda_{ik}^p
\,\delta_{\log(\lambda_{ij}/\lambda_{ik})}.
\tag{4}
\]

The law `\Delta_i` is unchanged if every eigenvalue of `A_i` is multiplied by the same positive scalar. It records only **relative logarithmic scale**.

### 1. Exact one-scale repairability criterion

The following are equivalent.

**(a) Some scalar blow-up is asymptotically tight.** There exist scales `s_i>0` such that the probability measures

\[
\nu_i^{(s_i)}
:=
\frac1{M_i}
\sum_j\lambda_{ij}^p
\,\delta_{\lambda_{ij}/s_i}
\qquad\text{on }(0,\infty)
\tag{5}
\]

are eventually uniformly tight; equivalently, for every `\varepsilon>0` there exist `C>1` and `i_0` such that

\[
\boxed{
\frac1{M_i}
\sum_{j:\ C^{-1}s_i\le\lambda_{ij}\le Cs_i}
\lambda_{ij}^p
\ge1-\varepsilon
\qquad(i\ge i_0).
}
\tag{6}
\]

**(b) Pairwise log-ratios are asymptotically tight.** For every `\varepsilon>0` there exist `R>0` and `i_0` such that

\[
\boxed{
\Delta_i([-R,R])\ge1-\varepsilon
\qquad(i\ge i_0).
}
\tag{7}
\]

Equivalently, with `C=e^R`,

\[
\boxed{
\frac1{M_i^2}
\sum_{j,k:\ C^{-1}\le\lambda_{ij}/\lambda_{ik}\le C}
\lambda_{ij}^p\lambda_{ik}^p
\ge1-\varepsilon
\qquad(i\ge i_0).
}
\tag{8}
\]

Thus:

\[
\boxed{
\text{some single scalar scale can retain the }p\text{-mass cloud}
\iff
\text{two }p\text{-mass samples have a tight relative log-ratio law}.
}
\tag{9}
\]

No preferred scale needs to be guessed in order to test the right-hand side.

### 2. A weighted median supplies an explicit repairing scale

Let `m_i` be any median of `\rho_i`, so

\[
\rho_i(( -\infty,m_i])\ge\frac12,
\qquad
\rho_i([m_i,\infty))\ge\frac12.
\tag{10}
\]

Set

\[
s_i:=e^{m_i}.
\tag{11}
\]

Then for every `R>0`,

\[
\boxed{
\rho_i\bigl(\{|x-m_i|>R\}\bigr)
\le
2\,\Delta_i\bigl(\{|u|>R\}\bigr).
}
\tag{12}
\]

Hence tightness of the scale-free pairwise difference laws immediately produces a tight scalar normalization. In multiplicative variables,

\[
\boxed{
\nu_i^{(s_i)}
\bigl((0,e^{-R})\cup(e^R,\infty)\bigr)
\le
2\,\Delta_i\bigl(\{|u|>R\}\bigr).
}
\tag{13}
\]

Conversely, for every center `a\in\mathbb R`,

\[
\boxed{
\Delta_i\bigl(\{|u|>2R\}\bigr)
\le
2\,\rho_i\bigl(\{|x-a|>R\}\bigr).
}
\tag{14}
\]

Equations (12) and (14) give a quantitative equivalence, not merely a compactness implication. If

\[
c_i(R):=
\inf_{a\in\mathbb R}
\rho_i(\{|x-a|>R\}),
\qquad
q_i(R):=
\Delta_i(\{|u|>R\}),
\tag{15}
\]

then

\[
\boxed{
 c_i(R)\le2q_i(R),
\qquad
 q_i(2R)\le2c_i(R).
}
\tag{16}
\]

Therefore the optimal one-scale concentration defect and the pairwise relative-scale defect vanish at infinity together.

### 3. Persistent separated mass is an exact no-single-scale obstruction

Suppose that along a cofinal subnet there are spectral sets `E_i,F_i\subset(0,\infty)` and a constant `\alpha>0` such that

\[
\frac1{M_i}\sum_{\lambda_{ij}\in E_i}\lambda_{ij}^p\ge\alpha,
\qquad
\frac1{M_i}\sum_{\lambda_{ij}\in F_i}\lambda_{ij}^p\ge\alpha,
\tag{17}
\]

while their logarithmic separation diverges:

\[
d_i
:=
\inf_{x\in E_i,\,y\in F_i}
\left|\log\frac{x}{y}\right|
\longrightarrow\infty.
\tag{18}
\]

Then for every fixed `R>0`, eventually `d_i>R`, and the two cross-events contribute at least

\[
\boxed{
\Delta_i(\{|u|>R\})\ge2\alpha^2.
}
\tag{19}
\]

Consequently `(\Delta_i)` is not tight and, by (9), **no sequence of scalar blow-up scales can make the full normalized `p`-mass tight**.

This is the precise multiscale obstruction only suggested qualitatively by AF-113. A second scale is fundamentally necessary when nonvanishing resource mass persists in logarithmically separating clusters; the obstruction is not tied to the operator norm or to any other particular attempted normalization.

### 4. AF-113's spike-plus-cloud failure is repairable by changing scale

Take the AF-113 family with one eigenvalue

\[
\delta_n=n^{-1}
\]

and

\[
N_n=\lfloor n^{2p}\rfloor
\]

eigenvalues

\[
\beta_n=n^{-2}.
\]

Its normalized `p`-mass at the top spike is

\[
a_n
:=
\frac{n^{-p}}{n^{-p}+N_n n^{-2p}}
\longrightarrow0,
\tag{20}
\]

while mass `1-a_n` lies at `\beta_n`. Therefore its log-ratio law is

\[
\Delta_n
=
\bigl(a_n^2+(1-a_n)^2\bigr)\delta_0
+a_n(1-a_n)
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr),
\tag{21}
\]

so

\[
\boxed{
\Delta_n\Longrightarrow\delta_0.
}
\tag{22}
\]

The pairwise criterion is tight even though the operator-norm blow-up in AF-113 collapses to its new boundary. Choosing instead

\[
s_n=\beta_n=n^{-2}
\tag{23}
\]

puts asymptotically all normalized `p`-mass at relative scale `1`.

Thus AF-113's control should be read sharply: it proves that **a canonical maximum scale need not be mass-coherent**. It does not prove that the same family is intrinsically multiscale. AF-114 separates those two failure modes.

### 5. A two-cloud family defeats every scalar normalization

Fix `p\ge1`. Let `A_n` be finite-rank positive diagonal with

\[
N_n:=\lfloor e^{pn}\rfloor
\]

eigenvalues equal to `e^{-n}`, and

\[
K_n:=\lfloor e^{2pn}\rfloor
\]

eigenvalues equal to `e^{-2n}`. Then

\[
\|A_n\|=e^{-n}\longrightarrow0,
\tag{24}
\]

and the two spectral clouds carry asymptotically equal `p`-mass:

\[
N_n e^{-pn}\longrightarrow1,
\qquad
K_n e^{-2pn}\longrightarrow1,
\qquad
M_n\longrightarrow2.
\tag{25}
\]

Hence `\rho_n` has asymptotic mass `1/2` near each of the two points `-n` and `-2n`. Its difference law has asymptotic masses

\[
\frac12\text{ at }0,
\qquad
\frac14\text{ at }n,
\qquad
\frac14\text{ at }-n.
\tag{26}
\]

More explicitly, if

\[
a_n:=\frac{N_ne^{-pn}}{M_n}\longrightarrow\frac12,
\tag{27}
\]

then

\[
\Delta_n
=
\bigl(a_n^2+(1-a_n)^2\bigr)\delta_0
+a_n(1-a_n)(\delta_n+\delta_{-n}).
\tag{28}
\]

Therefore for every fixed `R>0`,

\[
\boxed{
\lim_{n\to\infty}
\Delta_n(\{|u|>R\})
=\frac12.
}
\tag{29}
\]

No scalar choice `s_n` can make the normalized spectral `p`-mass tight in `(0,\infty)`. Centering one cloud necessarily sends the other to `0` or `\infty` in relative scale. This is a genuine two-level obstruction rather than a poor normalization choice.

## Derivation

The equivalence is elementary once the spectral data are moved to logarithmic scale.

Let `X_i,Y_i` be independent with law `\rho_i`, and let `m_i` satisfy (10). For the upper tail,

\[
\{X_i>m_i+R,\ Y_i\le m_i\}
\subseteq
\{X_i-Y_i>R\}.
\tag{30}
\]

Independence and the median property give

\[
\rho_i((m_i+R,\infty))\cdot\rho_i(( -\infty,m_i])
\le
\Delta_i((R,\infty)),
\]

hence

\[
\rho_i((m_i+R,\infty))
\le2\Delta_i((R,\infty)).
\tag{31}
\]

Similarly,

\[
\{X_i<m_i-R,\ Y_i\ge m_i\}
\subseteq
\{X_i-Y_i<-R\}
\]

gives

\[
\rho_i(( -\infty,m_i-R))
\le2\Delta_i(( -\infty,-R)).
\tag{32}
\]

Adding (31) and (32) proves (12).

For the converse, if both `X_i` and `Y_i` lie in `[a-R,a+R]`, then `|X_i-Y_i|\le2R`. Therefore

\[
\begin{aligned}
\Delta_i(\{|u|>2R\})
&\le
\mathbb P(|X_i-a|>R\text{ or }|Y_i-a|>R)\\
&\le
2\rho_i(\{|x-a|>R\}),
\end{aligned}
\tag{33}
\]

which proves (14). Taking the infimum over `a` gives the second inequality in (16); using `a=m_i` in (12) gives the first.

Since the logarithm is a homeomorphism `(0,\infty)\to\mathbb R`, tightness of `\nu_i^{(s_i)}` is exactly tightness of the translated measures

\[
(x-\log s_i)_\#\rho_i.
\tag{34}
\]

Equations (12)--(14) therefore prove the equivalence (a) `\Leftrightarrow` (b). Equation (8) is simply (7) written before taking logarithms.

For (19), if `X_i\in E_i` and `Y_i\in F_i`, or vice versa, then `|X_i-Y_i|>R` in logarithmic coordinates once `d_i>R`. Independence makes the two cross-probabilities at least `\alpha^2` each. The explicit calculations (21) and (28) then provide sharp controls for vanishing and persistent cross-scale mass.

## Exact controls and failure modes

### Pairwise log-ratio tightness is a repairability test, not a reconstruction theorem

The difference law `\Delta_i` is an autocorrelation-type compression. It is translation invariant by construction and generally does **not** determine `\rho_i` up to translation. Distinct homometric measures can share the same difference law, just as AF-004 shows that quadratic correlation or Fourier-magnitude data can lose phase and AF-005 shows that relational recovery depends on the full character lattice of retained couplings.

Accordingly, (9) certifies only that **some one-dimensional scale parameter is enough to prevent mass escape**. It does not recover the centered profile, eigenvalue provenance, phase, multiplicity marking beyond the weighted law, or any arithmetic discriminator.

### The median scale is constructive but not automatically admissible

The weighted median in (11) is determined from the complete `p`-mass profile and proves existence of a successful scalar normalization whenever one exists. An application may nevertheless forbid such an after-the-fact scale choice. If the intended compression permits only a source-derived geometric, arithmetic, or operator-theoretic scale, that admissibility restriction must be imposed separately.

Thus AF-114 classifies **geometric one-scale repairability**. It does not prove that a permitted or canonical scalar scale exists in a particular RH construction.

### Vanishing satellite mass does not create a multiscale obstruction

A spectral level can move arbitrarily far away in log scale without defeating one-scale tightness if its normalized `p`-mass tends to zero. This is exactly why the AF-113 spike is harmless after changing the center: its logarithmic separation diverges, but its contribution to the pairwise law vanishes.

The correct obstruction is persistent separated mass, not merely the existence of extreme eigenvalues or an unbounded spectral condition number.

### Tightness does not imply a unique limiting profile

Even after a successful centering, the family may have several weak cluster points. Prokhorov tightness gives precompactness, not convergence or uniqueness. A faithful downstream mechanism may still need a source law selecting one profile, the whole cluster set, or additional markings.

### Positivity and the `p`-mass weighting remain part of the object

The probability interpretation uses positive eigenvalues weighted by `\lambda^p`. For signed self-adjoint or nonnormal operators, cancellation and eigenvector geometry may require signed, singular-value, or marked measures instead. The pairwise-scale criterion should not be transferred unchanged merely by replacing the positive spectral law with a signed one.

### Relative-scale fidelity is still weaker than arithmetic fidelity

A matched Beurling/generalized-prime control may have exactly the same centered spectral mass law or the same pairwise ratio law. Before using a successful scale repair in an RH argument, the resulting retained structure must still separate rational-prime data from controls at the same information layer.

## Prior art and novelty assessment

The compactness mechanisms are classical. **No theorem-level novelty is claimed.**

- P.-L. Lions, **“The concentration-compactness principle in the Calculus of Variations. The locally compact case, part 1,”** *Annales de l'Institut Henri Poincaré C, Analyse non linéaire* 1(2), 109--145 (1984), DOI `10.1016/S0294-1449(16)30428-0`. Role: classical concentration-function and compactness-modulo-escape framework for probability mass in unbounded settings; the present logarithmic centering problem is an elementary one-dimensional specialization of the same compactness pressure.
- Pierre-Louis Lions, **“The Concentration-Compactness Principle in the Calculus of Variations. The limit case, Part 1,”** *Revista Matemática Iberoamericana* 1(1), 145--201 (1985), DOI `10.4171/RMI/6`. Role: classical treatment of loss of compactness generated by dilation invariance. After `x=\log\lambda`, scalar spectral dilation becomes ordinary translation, which is the symmetry quotiented in (9).
- Patrick Billingsley, ***Convergence of Probability Measures***, 2nd ed., Wiley (1999), DOI `10.1002/9780470316962`. Role: standard tightness, weak convergence, Portmanteau, and Prokhorov framework underlying the interpretation of a repaired family as weakly precompact.
- AF-004 and its phase-retrieval/higher-correlation sources delimit what the self-difference law cannot do: autocorrelation-type data need not determine an object up to the intended symmetry. AF-005 supplies the complementary character-lattice viewpoint for when additional relational couplings actually close such a quotient fiber.

Lions's concentration-compactness theory is much deeper and more general than the elementary median argument above, and the pairwise-difference criterion is proved here directly rather than asserted as a new concentration-compactness theorem. The durable Arithmetic Fidelity content is the placement of the classical compactness idea at the exact AF-113 frontier: **pairwise log-ratio tightness distinguishes a bad chosen blow-up scale from a genuine no-single-scale obstruction, without choosing the scale first.**

## Consequences for Arithmetic Fidelity

AF-112--AF-114 now separate three different compression events. Fixed unscaled probes can collapse an infinitesimal spectral cloud to its critical `p`-mass; a chosen scalar blow-up can restore relative shape but still fail because the chosen scale tracks negligible mass; and AF-114 decides whether that second failure can be repaired by *any* scalar normalization or whether persistent logarithmically separated resource mass forces a genuinely multiscale lift.

The resulting audit rule is scale-free. Before proposing a scalar renormalization, inspect the weighted pairwise ratio law. If it is tight, a one-scale repair exists in principle and a median supplies an explicit benchmark against which any claimed canonical scale can be tested. If it is not tight, searching for a better scalar normalization is futile: the representation needs a multiscale profile, marked hierarchy, renormalization tree, or a source theorem that rules out the separated-mass regime.

For later arithmetic applications, this also sharpens the meaning of provenance preservation. A global scalar scale can remove coherent drift, but it cannot preserve relations between two order-one arithmetic carriers whose characteristic scales diverge multiplicatively. Any RH mechanism that relies on both must either retain their relative logarithmic separation explicitly or prove that one carrier becomes negligible before compression.