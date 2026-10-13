# AF-566 — Almost-all short-interval primes make eight-probe minimax loss sharp

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · MULTIWAY-IDENTIFICATION · ALMOST-ALL-PRIME-INTERVALS · MINIMAX-SAMPLING · MATCHED-CONTROL · PREPRINT-EXTENSION-SEPARATED · NO-GENERAL-NOVELTY-CLAIM

## Claim: source locations can be selected from two simultaneous almost-all conditions

Use exactly AF-559's commonly registered prime-edit critical curves, AF-562's deterministic additive sup-norm experiment, AF-564's nonadaptive finite-probe design, and AF-565's normalized peak construction. The edit locations are **odd rational primes**, but the edited generator systems are **generalized-prime matched controls**. Let \(S\) range over finite sets of at least two such locations, and define
\[
M_k(P)=\inf_{\substack{S\subset\{\text{odd rational primes}\}\\
2\le |S|<\infty,\ \min S\ge P}}
\frac{\varepsilon_k(S)}{\varepsilon_{\rm full}(S)},\qquad
r_k=(3/2)^{1/k},\quad
u_k=\frac{\log r_k}{r_k-1},\quad
\vartheta_k=u_k e^{1-u_k},\quad
\beta_k=3-\frac{3}{r_k}.
\tag{1}
\]
AF-564 supplies the universal lower bound
\(\liminf_{P\to\infty}M_k(P)\ge\vartheta_k\)
for every fixed integer \(k\ge1\).

**Almost-all short-interval transfer theorem.** Suppose that for a fixed exponent \(\beta<\beta_k\), all but \(o(X)\) integers \(n\in[X,2X]\) have a rational prime in
\[
[n,n+X^\beta]
\tag{2}
\]
for every sufficiently large \(X\). Then, for every fixed \(k\ge2\), there are sets \(S_n\) of exactly \(2(k+1)\) odd rational-prime edit locations, with \(\min S_n\to\infty\), such that
\[
\frac{\varepsilon_k(S_n)}{\varepsilon_{\rm full}(S_n)}
\longrightarrow\vartheta_k.
\tag{3}
\]
Hence \(\lim_{P\to\infty}M_k(P)=\vartheta_k\) under (2). Crucially, the hypothesis **does not require** a prime within \(X^\beta\) of every sufficiently large real starting point, as AF-565's more restrictive pointwise argument did.

**Refereed unconditional consequence.** Guth--Maynard (2026), Corollary 1.4, gives (2) for every fixed \(\beta>2/15\). Since
\[
\beta_8=3-3(3/2)^{-1/8}=0.148260525\ldots>2/15,
\quad
\beta_9=0.132155765\ldots<2/15,
\]
we conclude **unconditionally using a peer-reviewed input** that
\[
\boxed{\displaystyle
\lim_{P\to\infty}M_k(P)
=\frac{\log((3/2)^{1/k})}{(3/2)^{1/k}-1}
 \exp\!\left(1-\frac{\log((3/2)^{1/k})}
 {(3/2)^{1/k}-1}\right)
\quad(1\le k\le8).}
\tag{4}
\]
For \(k=1\) sharpness was already known from AF-563; the new conclusion is \(3\le k\le8\), extending AF-565's unconditional \(k=2\) result. In particular \(\vartheta_3=0.997719822162\ldots\) and \(\vartheta_8=0.999678965432\ldots\).

## Lemma: a sparse exception set can be avoided at both shifted endpoints

Let \(X\to\infty\), let \(E_X\subset[X,2X]\cap\mathbb Z\) have \(|E_X|=o(X)\), and suppose \(\Delta:[X,3X/2]\to(0,\infty)\) is increasing, with \(\Delta=o(X)\) uniformly. For all sufficiently large \(X\), there is an integer \(n\in[X,3X/2]\) such that
\[
n\notin E_X,\qquad m(n):=\lfloor n+\Delta(n)\rfloor\notin E_X.
\tag{5}
\]
Indeed, \(n+\Delta(n)\) increases by more than one when \(n\) increases by one, so the integer map \(m(n)\) is injective. It also takes values in \([X,2X]\) for large \(X\). Thus at most \(2|E_X|=o(X)\) of the \(X/2+O(1)\) possible starts fail one of the two tests. If (2) holds, (5) provides primes
\[
p\in[n,n+X^\beta],\qquad q\in[m(n),m(n)+X^\beta].
\]
Whenever \(\Delta(n)/X^\beta\to\infty\) uniformly, these satisfy
\[
q-p=\Delta(n)+O(X^\beta+1)=\Delta(n)[1+o(1)].
\tag{6}
\]
The lemma needs neither independent randomness of the two primes nor pointwise prime-gap bounds. The injectivity of the shifted *integer starting point* is the essential simultaneous-selection step.

## Construction of all intermediate bottleneck pairs

By PNT and the mean of consecutive gaps on \([Y,2Y]\), take a sequence of consecutive odd primes \(p_0<q_0\to\infty\) with
\[
g=q_0-p_0=O(\log p_0),\qquad
d_0=\frac{2g}{e p_0^3\log p_0}.
\tag{7}
\]
Fix \(k\in\{2,\ldots,8\}\), put \(r=r_k\), and choose once and for all
\[
\frac{2}{15}<\beta<3-\frac3r=\beta_k.
\tag{8}
\]
For each \(1\le j<k\), set \(X_j=p_0^{r^j}\) (rounding to an integer changes nothing), and on \([X_j,3X_j/2]\) prescribe
\[
\Delta_j(v)=g\left(\frac{v}{p_0}\right)^3
                   \frac{\log v}{\log p_0}.
\tag{9}
\]
These functions are increasing, and since \(r^j<r^k=3/2\),
\[
\Delta_j(v)=o(X_j)
\quad\text{uniformly for }v\asymp X_j.
\tag{10}
\]
Moreover
\[
\frac{\Delta_j(v)}{X_j^\beta}
\asymp
g\,p_0^{\,r^j(3-\beta)-3}
\longrightarrow\infty
\quad(1\le j<k).
\tag{11}
\]
The exponent is smallest at \(j=1\) and is strictly positive because of (8). Equation (11) is exactly the prime-gap precision threshold in AF-565, but it need only be realized **for some suitable starting points**, not every one.

Apply Guth--Maynard's almost-all theorem at the scale \(X_j\), once to the original starting point and once to its increasing shifted image \(m_j(n)=\lfloor n+\Delta_j(n)\rfloor\). The lemma constructs odd primes \(p_j,q_j\) with
\[
p_j\asymp X_j,\quad
\frac{\log p_j}{\log p_0}\longrightarrow r^j,\quad
q_j-p_j=\Delta_j(p_j)[1+o(1)],\quad
\frac{q_j}{p_j}\longrightarrow1.
\tag{12}
\]
The replacement of \(\Delta_j(n)\) by \(\Delta_j(p_j)\) costs \(o(1)\) relatively: \(p_j-n=O(X_j^\beta)\) and \(\Delta_j'(v)/\Delta_j(v)=O(1/X_j)\). The pairs are widely separated and strictly ordered for large \(p_0\).

For the last pair use AF-562/AF-565's PNT construction
\[
Q=\frac{p_0^{3/2}}{2\sqrt g},\qquad
p_k\sim Q,\quad q_k\sim2Q,
\tag{13}
\]
with both locations odd primes. It is strictly above all the intermediate pairs, and \(\log p_k/\log p_0\to3/2=r^k\).

AF-559's uniform all-pair peak theorem now yields, for \(0\le j\le k\),
\[
D_{p_j,q_j}
=\frac{p_j^{-2}-q_j^{-2}}{e\log p_j}[1+o(1)]
=d_0[1+o(1)].
\tag{14}
\]
For the intermediate pairs this follows from (9),(12), since
\(p_j^{-2}-q_j^{-2}\sim2(q_j-p_j)/p_j^3\).
For the last pair it follows from \(Q^2=p_0^3/(4g)\) and
\(\log Q/\log p_0\to3/2\). As in AF-565, each intervening cross-pair gap has peak \(\gg d_0\): for \(j<k\),
\[
\frac{D_{q_j,p_{j+1}}}{d_0}
\asymp\frac{p_0^{3-2r^j}}{g}\longrightarrow\infty.
\tag{15}
\]
Thus AF-562's ordered adjacent-gap identity gives
\(2\varepsilon_{\rm full}(S)=d_0[1+o(1)]\) for
\(S=\{p_0,q_0,\ldots,p_k,q_k\}\).

## Exact \(k\)-probe optimization and boundary audits

Set \(x=c a\log p_0\), \(c=e^{B_1}\), and \(f(u)=u e^{1-u}\).
The *globally uniform* normalized response of AF-559 gives, for each of the fixed \(k+1\) bottleneck pairs,
\[
\sup_{x>0}\left|
\frac{\Phi_{q_j}(x/(c\log p_0))-
      \Phi_{p_j}(x/(c\log p_0))}{d_0}
-f(r^j x)\right|\longrightarrow0.
\tag{16}
\]
AF-565 has already solved the finite maximin problem exactly:
\[
\sup_{x_1,\dots,x_k>0}\min_{0\le j\le k}
\max_{1\le\ell\le k}f(r^jx_\ell)=\vartheta_k.
\tag{17}
\]
The upper bound uses the \(k+1\) separated peak scales and pigeonhole covering. The lower bound uses \(x_\ell=u_k/r^{\ell-1}\); each probe covers two neighboring scales at level \(\vartheta_k\), and (15) ensures the cross-pair gaps remain much larger than \(d_0\) at these fixed positive sample coordinates. Equations (14)--(17) prove (3) and then (4). \(\square\)

**Stress tests.** The selection lemma needs an increasing \(\Delta\), not merely \(\Delta=o(X)\); (9) is increasing, with \(\Delta'_j(v)>0\). The two exceptional-start sets are compared at the **same** dyadic scale, and the shifted map is injective; no unjustified probabilistic independence is used. The choice \(n\le3X/2\) keeps the shifted points inside the theorem's \([X,2X]\) range. The endpoint errors are \(O(X^\beta)\), negligible relative to the gap by (11), and \(q_j>p_j\) eventually. No assumption that \(p_j/X_j\to1\) is needed: \(\log p_j/\log p_0\to r^j\) suffices, while the *actual* prime \(p_j\) is used in the target gap (9). Only a fixed \(k\) is claimed; no simultaneous \(k\to\infty\) sharpness is inferred.

**Further, explicitly non-refereed extension.** Runbo Li's *preprint* “Primes in almost all short intervals” (arXiv:2407.05651, v6) announces (2) for any \(\beta>1/21.5\). If that preprint theorem is accepted as valid, the identical argument extends the sharp constants through \(k=25\), since \(\beta_{25}=0.04826337\ldots>1/21.5\) but \(\beta_{26}=0.04642153\ldots<1/21.5\). This is a clearly marked dependency on an unrefereed result, **not** part of the peer-reviewed unconditional claim (4). The argument for all \(k\ge9\) cannot be obtained from Guth--Maynard's \(2/15\) exponent alone.

## Prior art and relevance

The mean-value/PNT initial pair, last far pair, adjacent-gap reduction, uniform critical response, and equioscillating \(k\)-probe covering are from AF-559, AF-562, AF-564 and AF-565. The crucial external published input is Guth and Maynard, “New large value estimates for Dirichlet polynomials,” *Annals of Mathematics* 203(2), 623--675 (2026), DOI 10.4007/annals.2026.203.2.6, Corollary 1.4. Their almost-all prime distribution theorem is not new here. The line-specific derived contribution is the **two-endpoint injective-exception avoidance** that converts this weaker average information into AF-565's prescribed near-prime pair gaps, yielding sharp actual-prime-source minimax constants for six additional sample budgets.

This changes the finite-sampling frontier but not the underlying absolute information threshold. Each source family has a full-curve identification radius \(d_0/2\to0\); all bounds are relative to that vanishing margin, and the critical parameter registration is assumed known and shared. The generalized-prime edits are matched controls, not a demonstrated discriminator between rational primes and generalized primes at an RH-relevant output, and no implication for RH or an actual zero-exclusion mechanism follows without a separately verified arithmetic-to-zeros stability bridge.
