# RE-062 — bounded fan packets hide charge only through Egyptian cores or diverging depths

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + ADAPTIVE-FAN-SWITCH + BOUNDED-EVENT-PACKET + LAYER-UNIFORM-CHARGE-LAW + EGYPTIAN-CORE-COMPACTNESS + DEEP-LAYER-ESCAPE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-061` classifies the leading residual charge of a bounded fan-switch packet after passing to a subsequence with one fixed higher-layer depth multiset. That fixed-spectrum hypothesis is not innocuous: a bounded number of event depths may themselves drift to infinity, and a drifting tail can make reciprocal-depth mass disappear. The packet law nevertheless admits a complete layer-uniform classification. **For bounded packet cardinality, asymptotically vanishing selected-residual charge can occur only in two ways: every higher-layer depth escapes to infinity with no net fringe change, or a finite bounded-depth Egyptian core sums exactly to one while all remaining depths escape to infinity and the fringe changes `0 -> 1`.**

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

and fix

\[
J\Subset(1-\Theta,\tfrac12).
\tag{1}
\]

On an escaping sequence of sufficiently late common positive CA blocks from `RE-040`, let `b_n\in J` be rightmost-fan breakpoints and let

\[
C_{-,n}<C_{+,n}
\tag{2}
\]

be the consecutive **exposed fan states** tied at `b_n`. They may skip physical CA states. Put

\[
Y_{\pm,n}:=\log C_{\pm,n},
\qquad
Y_n:=Y_{-,n},
\qquad
L_n:=\log Y_n,
\tag{3}
\]

and assume that the complete physical CA event packet between the two exposed endpoints has cardinality at most one fixed `K`. Suppose the packet contains at least one higher-layer occurrence. Write its higher-layer depths, with multiplicity, as

\[
\mathcal J_n=\{j_{1,n},\ldots,j_{m_n,n}\},
\qquad
1\le m_n\le K,
\qquad
j_{i,n}\ge2,
\tag{4}
\]

and define

\[
s_n:=\sum_{i=1}^{m_n}\frac1{j_{i,n}}.
\tag{5}
\]

Let `\chi_{\pm,n}\in\{0,1\}` be the endpoint ordinary-fringe bits of `RE-059`--`RE-061`, and let `\mathcal R_b(Z)` be the translated nonlinear selected residual. Then the fixed-depth hypothesis of `RE-061` can be removed:

\[
\boxed{
Q_n
:=
\frac{b_n\sqrt{Y_n}}{L_n}
\left(
\mathcal R_{b_n}(Z_{+,n})-
\mathcal R_{b_n}(Z_{-,n})
\right)
=
-s_n+\chi_{+,n}-\chi_{-,n}+o_{J,K}(1).
}
\tag{6}
\]

The error in (6) is uniform over **all** higher-layer depths occurring in packets of cardinality at most `K`.

Consequently, if

\[
Q_n\longrightarrow0,
\tag{7}
\]

then every infinite subsequence has a further subsequence of one of the following two types:

1. **Deep-layer escape:**
   \[
   \chi_{+,n}=\chi_{-,n},
   \qquad
   \min_i j_{i,n}\longrightarrow\infty.
   \tag{8}
   \]
   Equivalently `s_n->0`. Every higher-layer generator is then subpower at the physical scale:
   \[
   p_{i,n}=Y_n^{o(1)}.
   \tag{9}
   \]

2. **Egyptian-core escape:**
   \[
   \chi_{-,n}=0,
   \qquad
   \chi_{+,n}=1,
   \tag{10}
   \]
   and, after reordering the depth slots, there is one fixed nonempty multiset
   \[
   \mathcal J_* = \{d_1,\ldots,d_r\},
   \qquad
   r\le K,
   \tag{11}
   \]
   such that
   \[
   \boxed{
   \sum_{a=1}^r\frac1{d_a}=1,
   }
   \tag{12}
   \]
   the corresponding `r` depths equal `d_1,...,d_r` eventually, and every remaining depth tends to infinity. The bounded core therefore lives on fixed power scales
   \[
   p_{a,n}=Y_n^{1/d_a+o(1)},
   \tag{13}
   \]
   while all noncore higher-layer generators are again `Y_n^{o(1)}`.

For each fixed `K` there are only finitely many possible core multisets `\mathcal J_*` satisfying (12). Thus a bounded fan packet cannot make its normalized source-bearing charge disappear by continuously tuning arbitrary finite depths. Up to subpower deep-layer tails, it must eventually use one of a finite catalogue of exact Egyptian resonances and the unique compensating endpoint pattern `0 -> 1`.

The special case in which no depth escapes to infinity recovers and strengthens the resonance conclusion of `RE-061`: after passage to a subsequence, an asymptotically cancelling bounded packet has one **fixed exact** reciprocal-depth spectrum from that finite catalogue.

## 1. The source-separated packet law is uniform in the layer depths

The first step is to return to the pre-depth form of `RE-061`. Let `\mathcal P_{\ge2,n}` be the multiset of higher-layer events in the packet and put

\[
H_n:=
\sum_{(p,j)\in\mathcal P_{\ge2,n}}\log p.
\tag{14}
\]

The bounded-packet geometry used in `RE-061` does not require fixed depths. Every physical event multiplies the CA state by its generating prime, and a packet containing at most `K` events satisfies

\[
Y_{+,n}-Y_{-,n}=O_K(L_n).
\tag{15}
\]

The tied endpoints have the same adaptive amplitude. The implicit tangent calculation of `RE-061` therefore gives

\[
Z_{+,n}-Z_{-,n}=O_K(L_n),
\qquad
Z_{\pm,n}\sim Y_n,
\tag{16}
\]

uniformly in the event depths. Every intervening event coordinate `\eta` lies at the same physical scale,

\[
\eta=Y_n(1+o_{J,K}(1)).
\tag{17}
\]

Now use the exact higher-layer event identity

\[
g(\eta_j(p))
=
\frac{\lambda_j(p)}{\log p},
\qquad
\lambda_j(p)
:=
\log\frac{1-p^{-(j+1)}}{1-p^{-j}}.
\tag{18}
\]

The Euler-tail jump is exactly `-lambda_j(p)`, while the higher-layer source mass jump is exactly `log p`. Since `N(Z)=sqrt(Z) log Z`, equations (17)--(18) give, uniformly in `j>=2`,

\[
N(Z)\lambda_j(p)
=
\frac{\log p}{\sqrt{Y_n}}(1+o_{J,K}(1)).
\tag{19}
\]

The corresponding `P=Phi_(>=2)` term contributes

\[
-\frac{1-b_n}{b_n}
\frac{\log p}{\sqrt{Y_n}}(1+o_{J,K}(1)).
\tag{20}
\]

Summing at most `K` occurrences, the two physical source contributions combine to

\[
-\frac{H_n}{b_n\sqrt{Y_n}}
+o_{J,K}\!\left(\frac{L_n}{\sqrt{Y_n}}\right).
\tag{21}
\]

Interior first-layer events remain negligible at this scale exactly as in `RE-061`. A nonzero endpoint fringe contributes

\[
\frac{\log r_{\pm,n}}
{b_n\sqrt{Y_n}}(1+o_{J,K}(1)),
\tag{22}
\]

with sign `+` at the upper endpoint and `-` at the lower endpoint. The common smooth terms in the residual vary over only `O_K(L_n)` in `Y` and `Z`; the bounds used in `RE-061` therefore remain `o_(J,K)(L_n/sqrt(Y_n))` without any fixed-depth input. Hence

\[
\boxed{
\mathcal R_{b_n}(Z_{+,n})-
\mathcal R_{b_n}(Z_{-,n})
=
\frac{-H_n
+\chi_{+,n}\log r_{+,n}
-\chi_{-,n}\log r_{-,n}}
{b_n\sqrt{Y_n}}
+o_{J,K}\!\left(\frac{L_n}{\sqrt{Y_n}}\right).
}
\tag{23}
\]

This is the layer-uniform form of `RE-061` equation (7). The only remaining issue is converting each `log p` into its reciprocal depth uniformly when `j` may grow.

## 2. Event coordinates recover reciprocal depth uniformly even when `j` grows

Put

\[
x:=p^{-j}\le\frac14.
\tag{24}
\]

Then

\[
\frac{1-p^{-(j+1)}}{1-p^{-j}}
=
1+u,
\qquad
u:=\frac{x(1-p^{-1})}{1-x}.
\tag{25}
\]

For every prime `p` and every `j>=2`,

\[
\frac{x}{2}\le u\le\frac{4x}{3}\le\frac13.
\tag{26}
\]

On `0<=u<=1/3`, the elementary bounds

\[
\frac{u}{1+u}\le\log(1+u)\le u
\tag{27}
\]

therefore give absolute constants `c_1,c_2>0` such that

\[
c_1p^{-j}
\le\lambda_j(p)
\le c_2p^{-j}
\tag{28}
\]

uniformly in both variables. In particular,

\[
\log\lambda_j(p)
=-j\log p+O(1).
\tag{29}
\]

The event equation (18) is equivalent to

\[
\eta_j(p)\log\eta_j(p)
=
\frac{\log p}{\lambda_j(p)}.
\tag{30}
\]

Taking logarithms and using (29),

\[
\log\eta_j(p)+\log\log\eta_j(p)
=
j\log p+\log\log p+O(1).
\tag{31}
\]

For an event in the bounded packet, (17) gives

\[
\log\eta_j(p)=L_n+o(1).
\tag{32}
\]

Since `p>=2` and `log p=O(L_n)`, equation (31) yields the layer-uniform relation

\[
\boxed{
j\log p=L_n+O(\log L_n),
}
\tag{33}
\]

and hence

\[
\boxed{
\frac{\log p}{L_n}
=
\frac1j
+O\!\left(\frac{\log L_n}{jL_n}\right).
}
\tag{34}
\]

Summing at most `K` higher-layer occurrences gives

\[
\boxed{
\frac{H_n}{L_n}
=s_n+O_K\!\left(\frac{\log L_n}{L_n}\right).
}
\tag{35}
\]

At a nonzero endpoint fringe, the unique unmatched ordinary prime satisfies `r=Z+O(1)` and `Z~Y_n`; therefore

\[
\frac{\log r_{\pm,n}}{L_n}=1+o_{J,K}(1).
\tag{36}
\]

Multiply (23) by `b_n sqrt(Y_n)/L_n` and insert (35)--(36). This proves the uniform packet law (6).

Equation (34) also gives the physical interpretation of a drifting depth. If `j_n->infinity`, then

\[
\frac{\log p_n}{\log Y_n}\longrightarrow0,
\tag{37}
\]

which is exactly `p_n=Y_n^{o(1)}`. For a fixed depth `d`, the same formula gives `p_n=Y_n^(1/d+o(1))`.

## 3. A compactness lemma classifies every vanishing reciprocal-depth mass

The relevant elementary lemma allows repeated denominators, as the CA packet may contain several events of the same depth.

**Bounded-length unit-fraction compactness.** Fix `K`. Let `\mathcal J_n` be multisets of at most `K` integers at least `2`, and suppose

\[
\sum_{j\in\mathcal J_n}\frac1j\longrightarrow s.
\tag{38}
\]

After passing to a subsequence and sorting the depth slots, each slot either becomes one fixed finite integer or tends to infinity. The finite slots form a multiset `\mathcal J_*` satisfying

\[
\sum_{d\in\mathcal J_*}\frac1d=s.
\tag{39}
\]

To see this, first pass to a subsequence with one fixed cardinality `m<=K`, sort

\[
j_{1,n}\le\cdots\le j_{m,n},
\]

and diagonalize over the finitely many slots in the one-point compactification `\{2,3,\ldots\}\cup\{\infty\}`. A finite limit must eventually be constant because the depths are integers; an infinite limit contributes zero reciprocal mass. Taking the limit of the finite sum proves (39).

When `s=1`, the finite core belongs to a finite catalogue depending only on `K`. Indeed, for an exact sorted representation

\[
1=\frac1{d_1}+\cdots+\frac1{d_r},
\qquad r\le K,
\tag{40}

the smallest denominator satisfies `d_1<=r`. Once `d_1,...,d_(a-1)` have been fixed, let

\[
R_a:=1-\sum_{i<a}\frac1{d_i}>0.
\tag{41}
\]

The remaining `r-a+1` terms are each at most `1/d_a`, so

\[
R_a\le\frac{r-a+1}{d_a},
\qquad
\boxed{
d_a\le\frac{r-a+1}{R_a}.}
\tag{42}
\]

Thus every denominator is recursively bounded after the preceding ones are chosen. There are only finitely many exact multisets (40) of length at most `K`.

This finiteness is classical Egyptian-fraction arithmetic; it is used here only as an elementary compactness input, not as a novelty claim.

## 4. Vanishing charge has exactly two asymptotic escape architectures

Assume (7). Since the endpoint difference

\[
d_n:=\chi_{+,n}-\chi_{-,n}
\tag{43}
\]

belongs to `{-1,0,1}`, pass to any infinite subsequence on which `d_n` is constant. Equation (6) gives

\[
s_n-d_n\longrightarrow0.
\tag{44}
\]

If `d_n=-1`, this is impossible because `s_n>0`. Therefore a vanishing-charge subsequence never has the fringe pattern `1 -> 0`.

If `d_n=0`, equation (44) gives `s_n->0`. Because all terms in (5) are positive and there are at most `K` of them,

\[
s_n\to0
\quad\Longleftrightarrow\quad
\min_i j_{i,n}\to\infty.
\tag{45}
\]

This is precisely the deep-layer escape (8), and (37) proves the subpower-generator statement (9).

If `d_n=1`, equation (44) gives `s_n->1`. Apply the compactness lemma with `s=1`. The finite depth slots form an exact core `\mathcal J_*` obeying (12), while every other slot tends to infinity. Since the only way to have `d_n=1` is `chi_-=0`, `chi_+=1`, this proves the Egyptian-core alternative (10)--(13). The finiteness argument (42) shows that, for fixed `K`, only finitely many bounded cores can occur.

This also identifies an important subtlety hidden by the fixed-spectrum formulation of `RE-061`. A nonexact full depth sum may approach one, for example by taking an exact core such as `(2,2)` and appending one depth `j_n->infinity`. Thus there is **no** uniform positive gap between one and all nonresonant `K`-term reciprocal sums once deep layers are allowed. The correct compact statement is resonance **modulo a vanishing deep tail**, not eventual exact resonance of the entire packet.

## 5. Stress tests and boundary of the result

The theorem classifies only the leading selected-residual scale `L/sqrt(Y)`. It does not prove that either escape architecture is realizable by genuine consecutive exposed fan states, and it does not resolve the smaller `1/sqrt(Y)` scale inside an Egyptian-core cancellation. A second-order charge could survive there, but `RE-061`'s present remainder is too coarse to assert it.

The bounded-cardinality hypothesis is essential. If the number of higher-layer events grows, reciprocal masses can be distributed among an increasing number of depths and the finite-slot compactness argument no longer gives a bounded resonance core. This finding therefore does not control fan switches whose skipped physical packet size diverges.

Nor does the classification itself contradict the polynomial fan complexity of `RE-051`. That theorem counts exposed states, while the present result constrains only those bounded packets whose normalized cross-cell charge tends to zero. A closing argument still needs to show that sufficiently many forced fan switches have bounded packets and cannot all use one of the two escape architectures.

The deep-layer alternative is genuinely different from the finite Egyptian resonances. Its generators satisfy `p=Y^(o(1))`, so the higher-layer source mass is `o(log Y)` even though a physical CA event is present. Eliminating it will require information about very deep prime-power layers or about how such events can occur between exposed adaptive maxima; first-layer short-interval input alone does not see this regime.

For the Egyptian-core alternative, the bounded part is much more rigid: fixed `K` leaves only a finite catalogue of exact reciprocal-depth cores, and each core forces a fixed collection of power scales `Y^(1/d)`. Extra deep events are asymptotically invisible at the leading charge scale. This gives a finite set of source architectures to test against the genuine CA event ordering and the fan-maximality geometry.

## 6. Prior-art and novelty boundary

A targeted current search of Egyptian-fraction compactness, colossally abundant transition packets, Robin counterexamples, and prime-layer event decompositions confirms that finiteness phenomena for fixed-length Egyptian representations are classical. The proof above is included because repeated depths are allowed and because the exact compactness statement needed here includes denominators escaping to infinity. No novelty is claimed for that elementary unit-fraction fact.

Mantovanelli's 2026 prime-layer workload remains the closest prior art for exact CA event packets and packet-mass bookkeeping; Zimov's 2025 work remains neighboring prior art for consecutive CA quotients. Both are already anchored in `SOURCES.md`. The search found no external result combining a false-RH adaptive fan residual with a layer-uniform reciprocal-depth compactness classification of bounded skipped CA packets.

The line-specific delta is therefore the removal of `RE-061`'s fixed-depth-spectrum assumption and the resulting exhaustion of all leading-order cancellation mechanisms for bounded packets. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

## Consequence

`RE-061` left an open-ended question about which varying depth spectra might repeatedly cancel higher-layer residual charge. The answer is now sharply restricted. For bounded physical packets, **there are only two asymptotic hiding places**:

\[
\text{all depths }\to\infty
\quad\text{with no net fringe change},
\]

or

\[
\text{one of finitely many exact Egyptian cores}
\quad+
\text{depths }\to\infty
\quad\text{with fringe }0\to1.
\]

The next source-sensitive target is therefore no longer an arbitrary packet spectrum. It is to exclude or control these two concrete architectures: deep subpower prime-power events between exposed fan states, and a finite list of fixed power-scale Egyptian cores with the unique compensating fringe pattern. Any bounded packet outside those classes carries a nonvanishing leading residual charge along some subsequence and cannot asymptotically hide at the `log Y/sqrt(Y)` scale.