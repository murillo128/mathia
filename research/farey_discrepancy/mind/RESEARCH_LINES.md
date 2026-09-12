# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Penetrate below the deterministic critical host scale

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-049--FD-055 reduce residual occupation collapse to a low-row source-localization problem and show that sufficiently strong short-interval cancellation transfers a zero-frontier spike to nearby nonsquarefree quadratic occupation.

FD-056--FD-058 distinguish sparse represented-start sampling from maximal ambient-window localization. A maximal source theorem can avoid the reciprocal-sample cardinality penalty, but its exceptional measure must still be smaller than the containing-start corridor at the desired transfer scale.

FD-059 identifies the deterministic critical scale `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`: favorable residue-class selection plus the one-Lipschitz source already forces a constant-fraction nonsquarefree twin at `q\asymp Q_X`. Along a false-RH zero-frontier spike this reaches the critical row exponent for every `\Theta>1/2` without short-interval input.

FD-060 shows that subpower slack above `Q_X` has more content than first-order accuracy. One can choose `K_X\to\infty`, `K_X\le\log\log Q_X`, and a squarefree host `q\asymp K_XQ_X` such that `q+1,\ldots,q+K_X` are all nonsquarefree and each retains at least `A_X/2-1` of the same physical spike. The resulting packet has total nonsquarefree quadratic occupation at least

\[
\frac{K_X}{\zeta(2)}\left(\frac{A_X}{2}-1\right)^2,
\]

and exceeds the selected host-row energy by an unbounded factor, while `K_X=X^{o(1)}` leaves the zero-frontier row power exponent unchanged.

The deterministic source bill is now localized more sharply. At `qA_X/X\asymp1`, bounded increments can guarantee only bounded packet length; a growing fixed-fraction packet requires `qA_X/X\to\infty`. For `qA_X/X\to0`, even fixed-fraction one-row transfer needs genuine source cancellation/localization or a different source-coupled mechanism. The live below-critical theorem is therefore to cross `X/A_X`, not merely to reproduce its exponent with subpower overhead.

## Convert packet amplification into global occupation control

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-060 improves the numerator locally but does not control the denominator. Its exact conclusion is

\[
U_{T,D}\gg K_XA_X^2
\]

for the constructed nonsquarefree packet and `U_{T,D}/J_q(T)\to\infty` against the selected squarefree host row. It does **not** imply `U_{T,D}/E_{T,D}\gg1`, because unrelated low rows may contribute much more than `K_XA_X^2` to `E_{T,D}`.

The decisive global question is therefore quantitative: on the same zero-frontier sequence and host construction, can the aggregate competing low-row energy outside the CRT packet be bounded at the packet scale `O(K_XA_X^2)` (or otherwise shown unable to swamp it)? A proof would turn the local packet into a global occupation statement; an admissible family with competing energy `\gg K_XA_X^2` would kill this route without undoing the packet theorem itself.

## Keep transfer accuracy, packet multiplicity, and global occupation as different currencies

At `qA_X/X\asymp1`, favorable host selection gives constant-factor one-row transfer. At `qA_X/X\to\infty`, the same deterministic budget may be spent either on relative error `o(1)` for one twin or on `K_X\to\infty` nonsquarefree rows retaining a fixed fraction. At `qA_X/X\to0`, bounded increments no longer suffice and source localization becomes essential.

Neither better one-row accuracy nor growing packet multiplicity alone controls `U/E`. Any argument using the zero-frontier exponent must therefore keep the hidden subpower factor `qA_X/X`, the attainable packet size, and the total competing energy explicit rather than treating equal power exponents as equivalent transfer strength.
