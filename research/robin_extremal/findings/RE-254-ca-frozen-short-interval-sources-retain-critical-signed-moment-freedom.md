# RE-254 — CA-frozen short-interval sources retain critical signed-moment freedom

**Status:** EXACT-DERIVED + DECISIVE-NEGATIVE/SOURCE-INFORMATION-OBSTRUCTION + ORDINARY-PRIME-ANCHORED-MATCHED-CONTROL + INTEGER-LABEL-ROBUSTNESS + PRIOR-ART-BOUNDED; independent adversarial audit pending.

**Dependencies:** RE-021 (ordinary CA frontier/selector), RE-022 (mixed Robin kernel), RE-252 (Guth–Maynard short-interval envelope), RE-253 (signed triangular moment), RE-246 and RE-248 (distinct remote generalized-prime transport obstructions).

RE-253 identifies a signed triangular prime-counting moment whose cancellation would make the first ordinary-prime Robin annulus negligible at the Guth–Maynard error-balance horizon. That cancellation **does not follow** from the uniform Guth–Maynard prime-counting estimate combined with an arbitrarily long, exactly ordinary-prime prefix containing the complete selected CA state. An explicit matched generalized-prime transport, including a strictly integer-labeled strengthening, preserves these inputs and changes the normalized critical moment by a fixed nonzero amount. The result concerns the information supplied by those hypotheses, not the behavior of ordinary primes or the sign of Robin's inequality.

## 1. Sharp local source-information obstruction

For an ordinary prime p tending to infinity, put
\[
L=\log p,\qquad e_p=\exp(-L^{1/4}),\qquad
H=H_\star(p)=\frac{p^{3/4}}{\sqrt L}\exp\left(\frac12L^{1/4}\right),
\qquad e_p H^2=\frac{p^{3/2}}L.
\tag{1}
\]
Fix any smooth nonnegative function \(\varphi\in C_c^\infty((1/4,3/4))\) with \(\int_0^1\varphi(u)\,du=1\), and a fixed amplitude \(a>0\). There are two indexed, strictly increasing, discrete real-label generalized-prime systems \(Q_p^+\), \(Q_p^-\), each obtained by order-preserving transport of the *actual ordinary primes*, with these properties for sufficiently large p:

1. Each indexed label outside \((p+H/4,p+3H/4)\) is unchanged, and every transported label remains inside that interval. Therefore both sources agree exactly with the ordinary primes through \(p+H/4\), have the same rank and shell cardinality, and satisfy adjacent-gap ratios \(1+O_a(Le_p)=1+o(1)\).
2. Writing \(\Pi_Q(t)=\#\{r\in Q:r\le t\}\), for one sufficiently large fixed \(x_0\) and a common implied constant independent of p and the sign, both sources satisfy the *all-start* Guth–Maynard-scale counting estimate
   \[
   \Pi_Q(x+y)-\Pi_Q(x)
   =\frac{y}{\log x}
     +O_{a,\varphi}\!\left(y e^{-(\log x)^{1/4}}\right),
   \quad x\ge x_0,\quad x^{3/5}\le y\le x^{0.99}.
   \tag{2}
   \]
   The constant is shared by the two signs but may depend on the fixed amplitude and bump. The original prime source satisfies the same qualitative estimate.
3. With the exact triangular source statistic
   \[
   D_{Q,p}(H)=\int_0^H\left(\Pi_Q(p+y)-\Pi_Q(p)-\frac yL\right)dy
   =\sum_{\substack{r\in Q\\p<r\le p+H}}\bigl(H-(r-p)\bigr)
      -\frac{H^2}{2L},
   \tag{3}
   \]
   the two values differ at precisely the unresolved RE-253 scale:
   \[
   \boxed{\frac{L}{p^{3/2}}\left(D_{Q_p^+ ,p}(H)-D_{Q_p^- ,p}(H)\right)
       =-2a+o(1).}
   \tag{4}
   \]
4. Define, solely as a source-model *local kernel*,
   \[
   \vartheta_Q(t)=\sum_{r\in Q,\ r\le t}\log r,\qquad
   h(t)=\frac{-\log(1-1/t)}{\log t},\quad k(t)=\frac1{t\log t},\quad
   I_Q(t)=(\vartheta_Q(t)-t)h'(t)-(h(t)-k(t)).
   \]
   Then the corresponding direct first-annulus integrals obey
   \[
   \boxed{\sqrt p\,L\int_p^{p+H}
       (I_{Q_p^+}(t)-I_{Q_p^-}(t))\,dt
       =2a+o(1).}
   \tag{5}
   \]

The statement holds for every sufficiently large ordinary prime p. In particular, if p is the first-layer frontier of a sufficiently large regular self-tangent *ordinary* colossally abundant integer C and X=log C, RE-021 gives \(X-p=O(p^{0.52})\). Since \(H/4\gg p^{0.52}\), the two systems agree with the ordinary primes well past X: the genuine ordinary CA exponent vector, its self-tangent selector, and all past prime-layer events are exactly frozen.

## 2. Explicit rank-preserving transport

Put \(s=aLe_pH\) and define increasing maps on the real axis by
\[
F_\pm(t)=t\pm s\varphi((t-p)/H).
\tag{6}
\]
The maps are the identity outside the displayed compact shell. Because
\[
\frac{s}{H}=aLe_p\longrightarrow0,\qquad
F_\pm'(t)=1\pm aLe_p\varphi'((t-p)/H)=1+o(1)
\tag{7}
\]
uniformly in t, both are increasing homeomorphisms for all large p, fixing both shell endpoints. Let
\[
Q_p^\pm=\{F_\pm(q):q\text{ is an ordinary prime}\},
\tag{8}
\]
with the prime index retained. This proves order preservation, exact exterior agreement, equal cardinality and gap-ratio control, including pairs straddling the shell endpoints. The positions need not be integers or ordinary primes; the construction makes no assertion that they are.

## 3. A uniform counting theorem for every interval start

Let \(G_\pm=F_\pm^{-1}\). For every real \(x,y>0\), the exact counting identity is
\[
\Pi_{Q_p^\pm}(x+y)-\Pi_{Q_p^\pm}(x)
=\pi(G_\pm(x+y))-\pi(G_\pm(x)).
\tag{9}
\]
If both interval endpoints lie outside the transport support, (9) is exactly the ordinary-prime count. Otherwise, for \(x^{3/5}\le y\le x^{0.99}\), the support geometry and \(y=o(x)\) imply \(x\asymp p\), in fact \(x/p\to1\). The inverse derivative satisfies \(G_\pm'=1+O_{a,\varphi}(Le_p)\). Consequently, with \(z=G_\pm(x)\) and \(w=G_\pm(x+y)-z\),
\[
z=x+O(s),\qquad
w=y(1+O_{a,\varphi}(Le_p)),\qquad
z/p\to1.
\tag{10}
\]

Apply the *pointwise*, not almost-all, Guth–Maynard corollary with a fixed \(\varepsilon<1/30\), say \(1/40\), to the ordinary prime count over \([z,z+w]\). The lower exponent \(17/30+1/40<3/5\) leaves room for the \(1+o(1)\) changes in z,w. Near the upper limit \(w=z^{0.99}(1+o(1))\), divide \([z,z+w]\) into two approximately equal intervals, both in the corollary's range. Replacing their individual logarithmic main terms by \(w/\log z\) costs
\(O(w^2/(z(\log z)^2))=o(we_p)\), because \(w\le z^{0.99}(1+o(1))\). Thus in the whole allowed range,
\[
\pi(z+w)-\pi(z)
=\frac{w}{\log z}+O(we_p).
\tag{11}
\]
Since \(|w-y|\ll yLe_p\), \(|\log z-\log x|=o(1)\) and \(\log x\sim L\), (11) yields
\[
\pi(z+w)-\pi(z)=\frac{y}{\log x}+O_{a,\varphi}(ye_p).
\]
For endpoint-affected intervals \(\exp(-(\log x)^{1/4})=(1+o(1))e_p\). Together with the unchanged-endpoint case this proves (2) for all real starts x and all allowed y, with one source-independent constant. No pointwise Chebyshev estimate for an arbitrary CA-selected prime was assumed.

## 4. Exact signed-moment separation and independent kernel check

At the horizon H every displaced point is fully contained in the sum (3). Therefore the triangular baseline cancels *exactly* between signs:
\[
D_{Q_p^+,p}(H)-D_{Q_p^-,p}(H)
=-2s\sum_{q\ {\rm prime}}\varphi((q-p)/H).
\tag{12}
\]
The sum is supported on a fixed interior proportion of the interval of length H. The same Guth–Maynard pointwise estimate, applied to \(\pi(p+v)-\pi(p)\) for \(v\asymp H\), and Stieltjes integration by parts give
\[
\sum_{q\ {\rm prime}}\varphi((q-p)/H)
=\frac H L\int_0^1\varphi(u)\,du+O_\varphi(He_p)
=\frac HL(1+O_\varphi(Le_p)).
\tag{13}
\]
It follows that (12) equals
\(-2a e_pH^2(1+o(1))=-2a p^{3/2}/L(1+o(1))\), proving (4). The sign is negative: moving primes right decreases their remaining triangular weight.

For (5), let \(b=p+H\), and write \(r_\pm=F_\pm(q)\) for each transported ordinary prime q. Exact integration of the two weighted Chebyshev steps, keeping their changed logarithmic weights, yields the positive identity
\[
\int_p^b (I_{Q_p^+}-I_{Q_p^-})(t)\,dt
=\sum_{q\ {\rm affected}}\int_{r_-}^{r_+}
\left[\frac1{t(t-1)}+\frac{h(b)}t\right]dt.
\tag{14}
\]
Indeed \((\log t)h(t)=-\log(1-1/t)\), whose derivative is \(-1/(t(t-1))\); the \(h(b)/t\) term is the indispensable terminal endpoint correction. On the transported shell
\[
\frac1{t(t-1)}+\frac{h(b)}t
=\frac1{p^2}\left(1+O(H/p+1/L)\right),
\tag{15}
\]
and \(r_+-r_-=2s\varphi((q-p)/H)\ge0\). Equations (13)–(15) give
\[
\sqrt p L\int_p^b (I_{Q_p^+}-I_{Q_p^-})
=\frac{\sqrt pL}{p^2}(2s)\frac HL(1+o(1))
=2a\frac{Le_pH^2}{p^{3/2}}(1+o(1))
=2a+o(1).
\]
This independent exact-kernel computation checks the normalization and sign without requiring RE-253's individual endpoint-remainder estimate. For selected p, RE-253 additionally provides that estimate for each source because the transformed labels have the same fixed prefix through p and comparable gaps.

## 5. Integer-label robustness without relaxing the all-start short-interval input

The obstruction (4)–(5) persists when **every transported source label is required to be a positive integer**. This is a strengthening of the same source-information statement, not an assertion that the moved labels remain prime.

For each original ordinary prime \(q\), round the two maps (6) to nearest integers:
\[
r_q^\pm=\left\lfloor F_\pm(q)+\frac12\right\rfloor,
\qquad
Q_{p,\mathbb Z}^\pm=(r_q^\pm)_{q\ {\rm ordinary\ prime}}.
\tag{16}
\]
Every original prime outside the support of \(\varphi((q-p)/H)\) is retained **exactly**, because then \(F_\pm(q)=q\in\mathbb Z\). Since that support is compactly contained in \((p+H/4,p+3H/4)\) and \(s/H=aLe_p=o(1)\), no altered label leaves the critical interior shell. In particular, the *entire* actual-prime prefix through \(p+H/4\), including the already selected CA exponent vector and selector, is unchanged.

**No collisions or rank changes.** For all sufficiently large \(p\), (7) gives \(F_\pm'(t)\ge3/4\) globally. On and across the modified shell, consecutive original odd primes \(q<q'\) have \(q'-q\ge2\); hence
\[
r_{q'}^\pm-r_q^\pm
\ge F_\pm(q')-F_\pm(q)-1
\ge \frac34(q'-q)-1
\ge\frac12>0.
\tag{17}
\]
The only consecutive-prime gap below two is the unaltered pair \(2,3\). Thus each rounded source is a strictly increasing integer sequence, with exactly the original rank, shell cardinality, and exterior labels. The integer labels may be composite; their integrality does not give the prime-atom divisor-sum law.

**All-start counting survives at the same error scale.** Each rounded label differs by at most \(1/2\) from its corresponding real label. The real labels that may move are separated by at least \(3/2\), so at any threshold \(t\), at most one label can cross \(t\) under rounding:
\[
\left|\Pi_{Q_{p,\mathbb Z}^\pm}(t)-\Pi_{Q_p^\pm}(t)\right|\le1.
\tag{18}
\]
Consequently every interval count differs by at most two. Because
\(x^{3/5}\exp(-(\log x)^{1/4})\to\infty\), this additive error is uniformly swallowed by the right-hand error in (2) for \(x\ge x_0\), after enlarging a *single* fixed \(x_0\) if necessary. In particular, both integer sources obey, with one implied constant independent of \(p\) and sign,
\[
\Pi_{Q_{p,\mathbb Z}^\pm}(x+y)-\Pi_{Q_{p,\mathbb Z}^\pm}(x)
=\frac{y}{\log x}
+O_{a,\varphi}\!\left(y e^{-(\log x)^{1/4}}\right),
\quad x^{3/5}\le y\le x^{0.99}.
\tag{19}
\]
This bound is for **all** admissible starts, not merely for intervals centered on \(p\).

**The critical signed discrepancy survives.** Let \(M\) be the number of ordinary primes in the critical shell. By Guth–Maynard, \(M=O(H/L)\); by (16), \(|(r_q^+-r_q^-)-2s\varphi((q-p)/H)|\le1\). Since both sources have the same shell count, (3) and (12) give the exact-centering comparison
\[
\begin{aligned}
D_{Q_{p,\mathbb Z}^+,p}(H)-D_{Q_{p,\mathbb Z}^-,p}(H)
&=-\sum_{p<q\le p+H}(r_q^+-r_q^-)\\
&=-2s\sum_q\varphi((q-p)/H)+O(H/L)\\
&=-\frac{2ap^{3/2}}{L}(1+o(1)).
\end{aligned}\tag{20}
\]
Here \(H/p^{3/2}\to0\), so the normalized rounding error is \(O(H/p^{3/2})=o(1)\). The limit in (4) remains exactly \(-2a\).

The corresponding kernel calculation is also exact, not an approximation that discards altered logarithmic jump weights. For \(b=p+H\), monotonicity of nearest-integer rounding gives \(r_q^+\ge r_q^-\), and the same integration by parts as (14) yields
\[
\int_p^b(I_{Q_{p,\mathbb Z}^+}-I_{Q_{p,\mathbb Z}^-})(t)\,dt
=\sum_{\text{affected }q}\int_{r_q^-}^{r_q^+}
\left[\frac1{t(t-1)}+\frac{h(b)}t\right]dt.
\tag{21}
\]
The kernel is \(p^{-2}(1+o(1))\) uniformly on this shell. The total effect of integer rounding on (21), after multiplication by \(\sqrt p L\), is \(O(H/p^{3/2})=o(1)\). Therefore
\[
\boxed{\quad
\frac{L}{p^{3/2}}\left(D_{Q_{p,\mathbb Z}^+,p}(H)
-D_{Q_{p,\mathbb Z}^-,p}(H)\right)=-2a+o(1),
\quad
\sqrt pL\int_p^{p+H}(I_{Q_{p,\mathbb Z}^+}-I_{Q_{p,\mathbb Z}^-})\,dt
=2a+o(1).
\quad}\tag{22}
\]

This rules out **integer labels alone** as an additional sufficient source-fidelity premise for the RE-253 critical little-\(o\) cancellation, even in the presence of the exact original CA prefix, fixed ranks and counts, and a common all-start short-interval PNT error envelope. It does not rule out genuinely prime-only arithmetic constraints, primality of every moved label, or a CA-conditioned result for ordinary primes.

## 6. Prior art, falsification, and the actual boundary

The external arithmetic input is Guth–Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026), 623–675, Corollary 1.3, DOI 10.4007/annals.2026.203.2.6. Smooth order-preserving point transport and generalized-prime flexibility are classical constructions (for generalized-prime context see W.-B. Zhang, *Normalization of Beurling generalized primes with Riemann Hypothesis*, Ann. Univ. Sci. Budapest. 39 (2013)). RE-246–RE-251 already distinguish source-fidelity from ordinary-prime arithmetic, but concern a *remote PNT-controlled terminal shell*, not RE-253's critical *near-p, all-start short-interval* signed statistic with the exact original CA prefix frozen. No generic novelty claim is made for smoothing, transport, nearest-integer rounding, Riesz means, or the external prime theorem. RE-250–RE-251 already treat integer/congruence-label quantization for a distinct, remote all-height PNT terminal kernel; Section 5 specifically retains integrality under the *near-frontier*, CA-prefix-frozen, all-start Guth–Maynard control of this finding. No new SOURCES.md anchor is needed.

Essential audit boundaries: (i) the smooth sources in Sections 1–4 have real labels and Section 5's integer-rounded sources have potentially composite labels; neither is a second possible set of ordinary primes; (ii) the CA selector is genuinely unchanged only because \(p+H/4\gg X\), not because a general synthetic source shares the ordinary divisor-sum law; (iii) the PNT implied constant is common across the two signs for each fixed a, not an arbitrarily preassigned sharp unit constant; (iv) the changed logarithmic jump weights are retained in (14), and after the shell \(\vartheta_Q\) need not equal ordinary \(\vartheta\) even though the *labels* outside the shell do; (v) the integral in (5) is a **source-model local kernel**. The actual finite value \(\sigma(C)/(C\log\log C)\) is unchanged, and one must not identify either altered source's global Euler-product/Mertens normalization with the ordinary Euler constant or claim a difference in genuine Robin heights.

Thus fixed ordinary-prime/CA prefix information plus the uniform Guth–Maynard prime-counting **error envelope alone** cannot force the RE-253 little-o signed moment at Hstar. An ordinary-prime-specific condition coupling future prime positions to the selected state (or stronger information than this counting envelope) is indispensable for that proposed route. The result neither asserts that actual primes exhibit the freedom, nor controls the remaining remote annulus, nor excludes a Robin counterexample, nor proves RH.