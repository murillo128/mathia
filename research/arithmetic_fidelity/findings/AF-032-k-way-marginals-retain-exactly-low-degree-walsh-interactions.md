# AF-032 — k-way marginals retain exactly the low-degree Walsh interactions

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let

\[
\Omega_d=\{-1,+1\}^d,
\]

let `M(\Omega_d)` be the real vector space of finite signed measures on `\Omega_d`, and for `A\subseteq[d]` let

\[
\pi_A:\Omega_d\to\{-1,+1\}^A
\]

be coordinate projection. For `0\le k\le d`, define the **k-marginal compression**

\[
\mathsf M_k(\mu)
=
\bigl((\pi_A)_*\mu\bigr)_{|A|\le k}.
\]

For `S\subseteq[d]`, write the Walsh character

\[
\chi_S(x)=\prod_{i\in S}x_i
\]

and its moment under `\mu`

\[
m_S(\mu)=\int_{\Omega_d}\chi_S(x)\,d\mu(x).
\]

Then:

1. **Marginal equality is exactly low-degree Walsh equality.** For any signed measures `\mu,\nu`,
   \[
   \boxed{
   \mathsf M_k(\mu)=\mathsf M_k(\nu)
   \iff
   m_S(\mu)=m_S(\nu)
   \quad\forall S\subseteq[d],\ |S|\le k.
   }
   \]

2. **The kernel is the pure high-order interaction space.** Define signed basis measures
   \[
   \eta_S(\{x\})=2^{-d}\chi_S(x).
   \]
   Then
   \[
   m_R(\eta_S)=\delta_{R,S},
   \]
   and therefore
   \[
   \boxed{
   \ker\mathsf M_k
   =
   \operatorname{span}\{\eta_S:|S|>k\}.
   }
   \]
   In particular,
   \[
   \boxed{
   \dim\ker\mathsf M_k
   =
   \sum_{j=k+1}^d\binom dj.
   }
   \]

3. **Marginal order gives an exact fidelity filtration.** Since
   \[
   \ker\mathsf M_d=\{0\}
   \subset\cdots\subset
   \ker\mathsf M_1
   \subset
   \ker\mathsf M_0,
   \]
   the information gained when passing from all `(k-1)`-way marginals to all `k`-way marginals is exactly the degree-`k` Walsh sector:
   \[
   \boxed{
   \ker\mathsf M_{k-1}/\ker\mathsf M_k
   \cong
   \operatorname{span}\{\eta_S:|S|=k\},
   }
   \]
   of dimension `\binom dk`.

4. **Every missing interaction order has genuine probability collisions.** Fix `S` with `|S|>k` and `0<\theta\le1`. Define
   \[
   P_{S,\theta}^{\pm}(\{x\})
   =
   2^{-d}\bigl(1\pm\theta\chi_S(x)\bigr).
   \]
   These are distinct probability measures and
   \[
   \boxed{
   \mathsf M_k(P_{S,\theta}^{+})
   =
   \mathsf M_k(P_{S,\theta}^{-}).
   }
   \]
   Thus the high-degree kernel is not merely a signed-measure artifact: every omitted Walsh character supplies a positive collision direction around the uniform law.

5. **Even all proper marginals can miss one global bit.** For `S=[d]` and `\theta=1`, let `P_+` and `P_-` be the uniform laws on the two parity classes
   \[
   \chi_{[d]}(x)=+1,
   \qquad
   \chi_{[d]}(x)=-1.
   \]
   Then every proper-coordinate marginal of `P_+` and `P_-` is the same uniform law, so
   \[
   \boxed{
   \mathsf M_{d-1}(P_+)=\mathsf M_{d-1}(P_-),
   }
   \]
   while
   \[
   m_{[d]}(P_+)=+1,
   \qquad
   m_{[d]}(P_-)=-1.
   \]
   Complete knowledge of every `(d-1)`-variable subsystem therefore need not determine the `d`-variable joint law.

6. **Restricted source classes remain a separate gate.** For an admissible family `\mathcal S\subset M(\Omega_d)`, exact `k`-marginal fidelity is
   \[
   \boxed{
   (\mathcal S-\mathcal S)
   \cap
   \operatorname{span}\{\eta_S:|S|>k\}
   =\{0\}.
   }
   \]
   Product laws, graphical models, deterministic constraints, or another structured family can therefore be recoverable from lower-order marginals only because the source class excludes the ambient high-order collision directions.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{complete information on every low-arity subsystem}
\not\Rightarrow
\text{global relational fidelity}.
}
\]

On the Boolean cube the loss is not qualitative: the entire missing sector is classified exactly by Walsh interaction degree.

## Fourier inversion on each marginal

Fix `A\subseteq[d]`. Write

\[
\mu_A=(\pi_A)_*\mu.
\]

For `S\subseteq A`, the Walsh coefficient of this marginal is

\[
\sum_{y\in\{-1,+1\}^A}
\mu_A(\{y\})\chi_S(y)
=
\sum_{x\in\Omega_d}
\mu(\{x\})\chi_S(x)
=
m_S(\mu).
\]

Fourier inversion on the finite abelian group `\{-1,+1\}^A` gives

\[
\boxed{
\mu_A(\{y\})
=
2^{-|A|}
\sum_{S\subseteq A}
 m_S(\mu)\chi_S(y).
}
\]

Therefore the marginal on `A` is determined exactly by the moments indexed by subsets of `A`. Knowing every marginal with `|A|\le k` is consequently equivalent to knowing every Walsh moment `m_S` with `|S|\le k`.

This proves item 1 without an asymptotic or genericity qualification.

## Exact kernel and interaction-order layers

For the basis measure

\[
\eta_S(\{x\})=2^{-d}\chi_S(x),
\]

orthogonality of Walsh characters gives

\[
\begin{aligned}
m_R(\eta_S)
&=
2^{-d}\sum_{x\in\Omega_d}\chi_R(x)\chi_S(x)\\
&=
2^{-d}\sum_x\chi_{R\triangle S}(x)\\
&=
\delta_{R,S}.
\end{aligned}
\]

The `2^d` measures `\eta_S` therefore form a basis dual to the full moment coordinates. By item 1, membership in `\ker\mathsf M_k` means precisely that all coordinates indexed by `|S|\le k` vanish. Hence

\[
\ker\mathsf M_k
=
\bigoplus_{|S|>k}\mathbb R\eta_S.
\]

This yields both the dimension formula and the filtration quotient

\[
\ker\mathsf M_{k-1}/\ker\mathsf M_k
\cong
\bigoplus_{|S|=k}\mathbb R\eta_S.
\]

So “interaction order” is an exact quotient invariant for this compression hierarchy. Moving from one marginal order to the next does not reveal an amorphous amount of extra dependence: it reveals exactly one homogeneous Walsh layer.

## Positive collisions and the parity extremizer

Let `U` be the uniform probability law on `\Omega_d`. Since

\[
P_{S,\theta}^{\pm}
=
U\pm\theta\eta_S,
\]

its atom masses are

\[
2^{-d}(1\pm\theta\chi_S(x)),
\]

which are nonnegative for `0<\theta\le1` and sum to one because every nonempty Walsh character has zero uniform mean.

If `|S|>k`, then for every `R` with `|R|\le k`,

\[
m_R(P_{S,\theta}^{+}-P_{S,\theta}^{-})
=2\theta\,m_R(\eta_S)
=0.
\]

Item 1 therefore gives identical `k`-marginal data.

At `S=[d]` and `\theta=1`,

\[
P_+(x)=2^{-d}(1+\chi_{[d]}(x)),
\qquad
P_-(x)=2^{-d}(1-\chi_{[d]}(x)).
\]

Each law is uniform on one parity half-cube. If any proper coordinate set `A` is fixed, at least one coordinate remains free. Exactly half of the completions have total parity `+1` and half have parity `-1`, so both induced marginals are uniform on `\{-1,+1\}^A`.

Thus the top interaction survives nowhere in the entire family of proper marginals yet changes the global law maximally. In the Walsh decomposition, the difference is literally a pure degree-`d` direction:

\[
P_+-P_-=2\eta_{[d]}.
\]

## Relation to AF-030 and AF-031

AF-030 classifies an arbitrary linear-test compression by the closed linear span of the tests actually retained. AF-031 then separates the joint feature law from the tuple of complete one-coordinate marginals.

The present result makes that relational loss **graded** on a canonical finite model. For the Boolean cube, the linear space generated by all observables depending on at most `k` coordinates is exactly

\[
\operatorname{span}\{\chi_S:|S|\le k\}.
\]

Its annihilator is therefore the high-degree sector found above. In other words, AF-030's abstract annihilator becomes an explicit interaction-order decomposition, while AF-031's coupling defect becomes a hierarchy rather than a single marginal-versus-joint gap.

This matters because “we retained all pairwise relations” or even “we retained every proper subsystem” is still not a structural recovery theorem. The exact question is whether the target discriminator has a component in an interaction sector above the maximum order actually retained.

## Prior art and novelty assessment

The mathematical mechanism is classical.

- Ryan O'Donnell, ***Analysis of Boolean Functions***, Cambridge University Press (2014), Chapter 1; corrected electronic version arXiv:`2105.10386`. Role: standard reference for the Walsh-Fourier basis on the Boolean cube, orthogonality, inversion, degree, and the interpretation of low-degree Fourier information.
- Noga Alon, Alexandr Andoni, Tali Kaufman, Kevin Matulef, Ronitt Rubinfeld, and Ning Xie, **“Testing k-wise and almost k-wise independence,”** *STOC 2007*, 496–505, DOI `10.1145/1250790.1250863`. Role: direct prior art relating `k`-wise independence of Boolean-cube distributions to low-order parity biases/Fourier coefficients; prevents treating the low-degree/marginal correspondence as new.
- Ronitt Rubinfeld and Ning Xie, **“Robust characterizations of k-wise independence over product spaces and related testing results,”** *Random Structures & Algorithms* 43(3) (2013), 265–312, DOI `10.1002/rsa.20423`. Role: broader product-space prior art showing that Fourier characterizations of bounded-order independence extend beyond the uniform Boolean setting.
- R. R. Bahadur, **“A Representation of the Joint Distribution of Responses to n Dichotomous Items,”** in *Studies in Item Analysis and Prediction*, Stanford University Press (1961), 158–168. Role: classical orthogonal expansion of multivariate binary distributions into progressively higher-order interaction terms; historical prior art for interpreting the missing Walsh sectors as higher-order dependence rather than as a new Arithmetic Fidelity object.

No novelty is claimed for Walsh analysis, `k`-wise independence, parity examples, Bahadur expansions, or the fact that lower-order marginals need not determine a joint distribution. The Arithmetic Fidelity contribution is the exact **compression audit**

\[
\mathsf M_k
\quad\longleftrightarrow\quad
\text{retain precisely interaction degrees }0,\ldots,k,
\]

with a closed-form kernel, a layer-by-layer quotient, and positive collision witnesses for every omitted character. This packages classical finite probability/Fourier facts into a sharp template for auditing claims that local, pairwise, finite-order, or subsystem-complete data preserve a global discriminator.

## Boundaries and failure modes

- The exact orthogonal grading uses the Boolean product group and its Walsh characters. Other finite product spaces have analogous character/tensor expansions, but the basis and interaction decomposition must be derived in the relevant category rather than assumed.
- Equality of all `k`-way marginals is stronger than matching only selected moments of order at most `k`; the theorem identifies them because on a finite binary marginal the full Walsh basis is available.
- Ambient high-degree ambiguity does not imply non-identifiability on every structured source family. The restricted-class intersection test in item 6 is mandatory.
- Interaction degree is representation-dependent. A nonlinear change of coordinates can move information between apparent orders, so an application must justify the feature decomposition intrinsically before treating low versus high order as structural.
- The theorem concerns exact recovery. Approximate low-degree control can bound some high-level observables under additional assumptions, but bounded or small low-degree coefficients do not by themselves imply a small global distributional error.
- For `k=d`, the compression contains the full joint law and the kernel vanishes, as it must.
- No arithmetic-specific claim follows from the parity example. A prime application must identify an intrinsic decomposition into channels/subsystems and show that the prime discriminator genuinely occupies an omitted interaction sector rather than importing this finite analogy rhetorically.

## Consequences for the research line

AF-031 established that complete marginal channels can erase coupling. AF-032 gives a sharper stopping rule whenever a proposed representation is assembled from many components:

\[
\boxed{
\text{Determine the highest interaction order genuinely retained,
then compute what lives above it.}
}
\]

If a compression stores all subsystem laws only up to order `k`, every downstream deterministic operation still factors through `\mathsf M_k` and therefore cannot recreate an omitted high-order interaction. A proposed boundary, marking, phase, transverse, operator, or arithmetic lift must either retain the relevant mixed relation explicitly or prove that the admissible source class forces that higher-order sector from lower-order data.

For later rational-prime use, this warns against a particularly strong but false inference: even exact agreement of **every proper local subsystem** with a matched control need not imply equality of the global object. Prime-specific provenance could, in principle, live in a genuinely global interaction sector. Demonstrating that it does is a separate theorem; the present result supplies the exact finite model of what such a claim would have to mean.